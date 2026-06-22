#!/usr/bin/env bash
#
# Installiert eine bestimmte Typst-Version projektlokal ins venv (.venv/bin/typst).
#
# Hintergrund: jupyter-book / mystmd ruft das `typst` vom PATH auf und erzeugt fuer
# `\partial` noch das alte Symbol `diff`, das ab Typst 0.14 deprecated und ab 0.15
# entfernt ist. Mit einer aelteren Typst-Version (Standard: 0.13.0) im venv laeuft
# der `jupyter book build --typst`-Export wieder durch, ohne die globale
# (Homebrew-)Installation anzutasten -- die venv-Kopie hat bei aktivem venv Vorrang.
#
# Verwendung:
#   ./install-typst-venv.sh            # installiert Standardversion (0.13.0)
#   ./install-typst-venv.sh 0.13.0     # installiert eine bestimmte Version
#
# Rueckgaengig: einfach .venv/bin/typst loeschen.

set -euo pipefail

TYPST_VERSION="${1:-0.13.0}"

# venv finden: aktives venv bevorzugen, sonst ./.venv relativ zum Script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${VIRTUAL_ENV:-$SCRIPT_DIR/.venv}"

if [ ! -d "$VENV_DIR/bin" ]; then
  echo "Fehler: venv nicht gefunden unter '$VENV_DIR'." >&2
  echo "Aktiviere zuerst dein venv (source .venv/bin/activate) oder lege es an." >&2
  exit 1
fi

# Plattform/Architektur auf das Typst-Release-Namensschema abbilden.
os="$(uname -s)"
arch="$(uname -m)"
case "$os" in
  Darwin) os_part="apple-darwin" ;;
  Linux)  os_part="unknown-linux-musl" ;;
  *) echo "Fehler: nicht unterstuetztes OS '$os'." >&2; exit 1 ;;
esac
case "$arch" in
  arm64|aarch64) arch_part="aarch64" ;;
  x86_64|amd64)  arch_part="x86_64" ;;
  *) echo "Fehler: nicht unterstuetzte Architektur '$arch'." >&2; exit 1 ;;
esac

target="${arch_part}-${os_part}"
url="https://github.com/typst/typst/releases/download/v${TYPST_VERSION}/typst-${target}.tar.xz"

echo "Lade Typst ${TYPST_VERSION} fuer ${target} ..."
tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

if ! curl -fSL "$url" -o "$tmpdir/typst.tar.xz"; then
  echo "Fehler: Download fehlgeschlagen ($url)." >&2
  echo "Existiert die Version v${TYPST_VERSION}? Siehe https://github.com/typst/typst/releases" >&2
  exit 1
fi

tar -xf "$tmpdir/typst.tar.xz" -C "$tmpdir"
bin_src="$tmpdir/typst-${target}/typst"

if [ ! -x "$bin_src" ]; then
  echo "Fehler: typst-Binary im Archiv nicht gefunden." >&2
  exit 1
fi

cp "$bin_src" "$VENV_DIR/bin/typst"
chmod +x "$VENV_DIR/bin/typst"

echo "Installiert nach: $VENV_DIR/bin/typst"
echo -n "Version: "
"$VENV_DIR/bin/typst" --version

# Kurzer Funktionstest fuer das von mystmd erzeugte `diff`-Symbol.
if printf '#set page(width: auto, height: auto)\n$ frac(diff f, diff x) $\n' \
   | "$VENV_DIR/bin/typst" compile - "$tmpdir/check.pdf" >/dev/null 2>&1; then
  echo "OK: 'diff'-Symbol wird unterstuetzt -- jupyter book build --typst sollte laufen."
else
  echo "Warnung: 'diff'-Test fehlgeschlagen -- diese Typst-Version ist evtl. inkompatibel." >&2
fi
