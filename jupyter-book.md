# Jupyter Book & PDF-Export (Typst)

## Installation

Voraussetzung: ein venv im Repo-Root (`.venv`).

```bash
# venv aktivieren
source .venv/bin/activate

# Jupyter Book (mystmd) installieren
uv pip install jupyter-book        # oder: pip install jupyter-book

# Typst 0.13 ins venv installieren (NICHT 0.15 – siehe unten)
./install-typst-venv.sh
```

`install-typst-venv.sh` legt eine projektlokale `typst`-Binary nach `.venv/bin/`.
Die globale (Homebrew-)Installation bleibt unangetastet; rückgängig: `.venv/bin/typst` löschen.

## Build

Im Ordner mit der `myst.yml` (hier `Numerische-Grundlagen-FS26/`):

```bash
jupyter book build --typst     # PDF nach exports/
jupyter book build --html      # HTML-Site
jupyter book start             # lokale Vorschau
```

## Warum Typst 0.13?

mystmd erzeugt für `\partial` das alte Typst-Symbol `diff`, das ab Typst **0.14**
deprecated und ab **0.15** entfernt ist. Mit Typst **0.13** läuft der Export sauber.
Bei aktivem venv hat `.venv/bin/typst` Vorrang vor dem globalen Typst.

## Worauf beim Schreiben der Notebooks achten (für den PDF-Export)

Der mystmd→Typst-Konverter unterstützt nicht alles, was KaTeX/LaTeX kann. Vermeiden:

- **`\left`/`\right` nur mit normalen Klammern** `( ) [ ] \{ \} |`.
  Nicht: `\left]…\right[` (offene Intervalle), `\left\langle…\right\rangle`.
  → Brackets ohne `\left`/`\right` schreiben, z.B. `]0,1[`, `\langle f,g \rangle`.
- **Kein `\displaystyle`** in Inline-Mathe. Für große Darstellung `$$…$$` nutzen.
- **Seltene Makros ersetzen:**
  - `\longrightarrow` → `\to`
  - `\mp` → Unicode `∓`
  - `\argmin` / `\argmax` → `\operatorname*{argmin}` (ohne `\,` im Argument)
- **Keine nackten URLs mit Klammern** (`(` `)` in der URL). Immer `[Text](url)` verwenden,
  sonst scheitert Typst am Auto-Link.
- **Animationen** (`FuncAnimation`): nicht `HTML(ani.to_jshtml())`, sondern als GIF
  speichern und anzeigen – funktioniert in HTML und PDF:
  ```python
  ani.save("name.gif", writer="pillow", fps=20)
  plt.close(fig)
  from IPython.display import Image
  Image(filename="name.gif")
  ```
- **Wikipedia-Links** ohne `#/media/…`-Anker; auf Commons-Dateiseite verlinken
  (`https://commons.wikimedia.org/wiki/File:…`).

> Faustregel: Wenn `typst compile` mit `unknown variable: <wort>` abbricht, wurde ein
> LaTeX-Makro nicht übersetzt – das betreffende Symbol durch ein Standard-Primitiv
> oder Unicode ersetzen.
