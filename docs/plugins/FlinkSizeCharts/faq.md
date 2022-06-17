# Wie muss die CSV für den Import einer Größentabelle aussehen?

Mit einer CSV Datei können mehrere Reiter gleichzeitig angelegt werden. Die Datei sollte dafür folgendermaßen
aufgebaut sein:

<table>
<tbody>
<tr><td>Name Reiter 1</td><td></td><td></td></tr>
<tr><td>Titel Spalte 1</td><td>Titel Spalte 2</td><td>Titel Spalte 3</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>&nbsp;</td><td></td><td></td></tr>
<tr><td>Name Reiter 2</td><td></td><td></td></tr>
<tr><td>Titel Spalte 1</td><td>Titel Spalte 2</td><td>Titel Spalte 3</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
<tr><td>Wert</td><td>Wert</td><td>Wert</td></tr>
</tbody>
</table>

**Wichtig:** 
- Zwischen den Definitionen für zwei Reiter muss wie im Beispiel oben eine leere Zeile eingefügt werden!
- Die CSV-Datei sollte mit dem Zeichensatz UTF-8 gespeichert werden. In Excel gibt es dazu beim Speichern der Datei
  eine Option im Dropdown des Dateiformats ("CSV UTF-8")

Hier kann eine Beispieldatei heruntegeladen werden: [CSV Import Beispieldatei](./files/sizechart-sample-import.csv)