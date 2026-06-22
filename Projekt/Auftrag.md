# Gruppenprojekt: Detaillierte Analyse von Wetterdaten

## Projektübersicht

In diesem Projekt arbeitet ihr in 2er- bis 3er-Gruppen (Gruppeneinteilung auf Moodle). Die Bewertung der Arbeit trägt mit 40% zur Endnote des Moduls bei.

Euer Ziel ist es, mit Wetterdaten zu arbeiten und diese zu analysieren. Die Daten stammen von [MeteoSchweiz](https://gate.meteoswiss.ch/) und werden in CSV-Dateien im Ordner `Daten` zur Verfügung gestellt. Darin ist auch eine Legende zu den Bezeichnungen der Wetterstationen und den Messwerten enthalten.

Die Daten umfassen Messungen zu Luftdruck, Temperatur, Regenmenge, und Sonnenstunden über ein Jahr, jeweils gemittelt über eine Stunde. Wir haben 15% der Datenpunkte entfernt, um Lücken zu schaffen, die ihr interpolieren müsst. (Es gibt keine "Missing Values" in den Daten, sondern es gibt einfach nicht zu jeder Stunde einen Messwert.)

## Aufgabenstellung

Die folgenden Punkte sollen abgearbeitet werden. Details findet ihr in der Projekt-Vorlage `Projekt_Vorlage.ipynb`.

1. Daten importieren und bereinigen
2. Interpolation
3. Daten und Interpolation darstellen und vergleichen
4. Nullstellen der Temperatur bestimmen
5. Grosse Schwankungen in Temperatur oder Luftdruck finden
6. Mittelwerte berechnen
7. Glättung (Gleitendes Mittel) bestimmen

## Abgabe

Folgende Dateien sind abzugeben:

- Ein **Jupyter-Notebook** mit Code, Visualisierungen und Dokumentation / Erklärungen der Schritte.
- Eine **Präsentation als PDF**, die euer Vorgehen, Ergebnisse und Schlussfolgerungen zusammenfasst.
- Ein **Video** (oder Link zu einem Video), in dem die Präsentation vorgestellt wird (max. 10 Minuten).

Die Dateinamen sollen wie folgt lauten: `NGDS_FS26_Projekt_Gruppe_X.*`, wobei `X` dem Gruppennamen entspricht.

Eine Abgabe-Aktivität wird auf Moodle noch zur Verfügung gestellt. Abgabe-Termin ist der **Sonntag, 26. April 2026, 23:59 Uhr**.


## Anforderungen an das Jupyter-Notebook

- **Code-Strukturierung:** Stellt sicher, dass euer Code übersichtlich gegliedert und verständlich kommentiert ist. Ziel ist es, dass Dritte euren Code problemlos lesen, nachvollziehen und ausführen können.

- **Dokumentation:** Nutzt Markdown-Zellen, um euren Analyseprozess Schritt für Schritt zu dokumentieren. Erklärt eure methodischen Entscheidungen, den Ablauf der Berechnungsschritte und die Interpretation der Ergebnisse.

- **Datenimport:** Konfiguriert euer Notebook so, dass es die CSV-Datei aus dem Ordner `Daten` relativ zum Notebook importiert. Das heisst, es soll lauffähig sein, wenn es im NGDS-Repository im Ordner `Projekt` ausgeführt wird. Nutzt dazu Funktionen aus NumPy und nicht die Pandas-Bibliothek.

- **Visualisierungen:** Erstellt klare und aussagekräftige Visualisierungen, die eure Daten und Analysen unterstützen. Jedes Diagramm soll korrekte Achsenbeschriftungen mit Einheiten haben und eine Legende, wenn mehr als ein Graph dargestellt ist. Unter dem Diagramm soll in einer Markdown Zelle eine kurze Beschreibung der Abbildung stehen, die den Inhalt und die Bedeutung erläutert.

- **Zusammenfassung:** Fügt am Ende des Notebooks eine kurze und klare Zusammenfassung eurer Hauptergebnisse und Schlussfolgerungen an. Diese sollte die wesentlichen Erkenntnisse eurer Arbeit hervorheben.

- **Reflexion:** Schliesst das Notebook mit einer kurzen Reflexion zum Prozess der Gruppenarbeit ab, einschliesslich der Rollenverteilung und des Beitrags jedes Mitglieds. Diskutiert, was gut funktioniert hat und wo es Verbesserungspotenzial gibt.

## Anforderungen an die Präsentation

- **Zeitplanung:** Das Video der Präsentation darf maximal 10 Minuten dauern.
  
- **Inhalt:** Konzentriert euch auf die Darstellung der Kernergebnisse und wichtigsten Erkenntnisse aus eurem Projekt. Die Präsentation muss einen klaren Überblick über eure Analyseergebnisse und Schlussfolgerungen bieten.

- **Teamarbeit:** Alle Mitglieder der Gruppe müssen aktiv an der Präsentation teilnehmen und einen gleichwertigen Teil des Vortrags übernehmen.

- **Visualisierungen:** Integriert aussagekräftige und selbsterklärende Grafiken und Diagramme, die eure Ergebnisse und Analysen unterstützen. Vermeidet überladene oder komplizierte Visualisierungen und Folien.

- **Code-Darstellung:** Beschränkt die Einbindung von Code in die Präsentation auf das notwendige Minimum. Wenn Code gezeigt wird, muss dieser klar und direkt zur Erklärung des Vorgehens und/oder Ergebnisse beitragen.

- **Kommunikation:** Verwendet eine klare, präzise und für das Publikum verständliche Sprache.

Für Fragen oder Unterstützung stehen wir gerne zur Verfügung. Viel Erfolg!

## FAQ

- Dürfen auch andere Packages (wie Pandas und Seaborn) verwendet werden, die nicht in NGDS unterrichtet werden?
  - Grundsätzlich ja, allerdings sind alle Aufgaben eher einfacher mit NumPy, SciPy und Matplotlib lösbar.
- Dürfen auch 1er oder 4er Gruppen gebildet werden?
  - Nein, das Projekt ist für 2er- und 3er-Gruppen ausgelegt.