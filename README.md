## Schönen guten Tag Herr Hergaß,
Da ist zu viel Langeweile habe, habe ich 2 Versionen des Spiels erstellt, da ich keine Lust hatte, beide Versionen zusammenzufassen. Sie benötigen nach meinem Wissenstands keine weiteren Dinge, um die normale Version (ezmode) zu spielen. Um den Hardmode zu spielen, benötigen Sie allerdings das Paket "zufallsworte", welches Sie mit "pip install zufallsworte" installieren können. Falls Sie darauf bestehen, dass ich beide Dateien zusammenführen soll, werde ich dies natürlich tun, doch bitte sehen Sie davon ab, da ich abgeneigt bin, da zu tun.

Jetzt zu den Spielen.

ezmode:
Spieler: >= 2
Ein Spieler gibt nach Programmstart ein Wort ein, welches verdeckt wird, damit die anderen Spieler dieses nicht sehen. Dann bekommt der andere Spieler gesagt, wie viele Buchstaben das Wort hat. Dieser Spieler muss nun das Wort korrekt erraten, indem er immer einen Buchstaben eingibt. Falls dieser Buchstabe nicht im Wort vorhanden ist, wird ein Versuch abgezogen. Es wird ebenfalls ein Versuch abgezogen, wenn der Spieler einen Buchstaben errät, der davor schon geraten wurde. Wenn der Spieler keine Versuche mehr übrig hat, wird das Programm beendet und das Wort ausgegeben.

hardmode:
Spieler: >= 1
Der Spieler spielt gegen das Programm. Es wird zufällig ein Wort mit der Länge 2-28 Buchstaben ausgewählt. Der Spieler weiß nur, wie lang das Wort ist. Er hat nun anstatt 10 12 Versuche, doch bekommt alle abgezogen, wenn er ein Buchstaben doppelt rät. Sonst ist alles identisch.
