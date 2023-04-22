from getpass import getpass
import re

n = 10                                                                                                                                                      # Versuche des Spielers, bis dieser verloren hat
wort_erraten = False                                                                                                                                        # Angabe, ob das Wort erraten wurde
geratene_buchstaben = []                                                                                                                                    # leere Liste für Buchstaben, die schon erraten wurden

wort = getpass("Gib ein beliebiges Wort an, welches mehrere Buchstaben hat: \n").lower()                                                                    # Eingabe eines Worts, welches in der Konsole versteckt wird. Alle Buchstaben werden klein gemacht

if re.findall('\d+', wort):                                                                                                                                 # Überprüfung, ob sich Zahlen im Wort befinden
    print("Welches Wort beinhaltet denn bitte Zahlen? \nDu Idiot. \nVersuche es nocheinmal ohne Zahlen!")                                                   # Ausgabe, wenn sich Zahlen im Wort befinden
    exit()                                                                                                                                                  # Das Programm wird terminiert

wort_liste = list(wort)                                                                                                                                     # Eine Liste mit allen Buchstaben des Worts wird erstellt
wort_leerstellenliste = ["_" for i in range(len(wort))]                                                                                               		# Anhand von der Anzahl der Buchstaben wird bestimmt, wie viele leere Striche kreiert werden müssen
print("Anzahl der verbleibenden Versuche:", n)                                                                                                              # Ausgabe Anzahl Fehlversuche
print("Das Wort hat", len(wort), "Buchstaben.")                                                                                                       		# Ausgabe Anzahl Buchstaben im Wort


while n > 0 and not wort_erraten:
    buchstabe = input("Gib einen Buchstaben an, welchen du im Wort vermutest: \n")[0].lower()                                                               # Eingabe eines! Buchstabens. Wird mit .lower() kleingemacht, damit es keine Probleme gibt.

    if buchstabe in geratene_buchstaben:                                                                                                                    # Überprüfung, ob ein Buchstabe bereits geraten wurde
        print("Du hast diesen Buchstaben bereits geraten, du Idiot. Du bekommst für deine Dummheit 1 Versuch abgezogen. Jetzt mach mal richtig.")
        n -= 1
        print("Anzahl der verbleibenden Versuche:", n)

    geratene_buchstaben.append(buchstabe)																													# Hinzufügen des geratenen Buchstabens zur Liste

    if buchstabe in wort_liste:                                                                                                                             # Überprüfung, ob der Buchstabe im Wort vorhanden ist
        print("Der Buchstabe", buchstabe, "befindet sich im Wort.")

        for i in range(len(wort)):                                                                                                                    		# Schleife über alle Buchstaben des Worts
            if wort_liste[i] == buchstabe:                                                                                                                  # Überprüfung, ob der Buchstabe am Index i im Wort vorhanden ist
                wort_leerstellenliste[i] = buchstabe                                                                                                        # Wenn ja, wird die passende Leerstelle mit dem Buchstaben ersetzt
        print(" ".join(wort_leerstellenliste))                                                                                                              # Ausgabe des aktuellen Zustands des Worts als String, inklusive der erratenen Buchstaben
        
        if "_" not in wort_leerstellenliste:                                                                                                                # Überprüfung, ob noch Platzhalter vorhanden sind
            wort_erraten = True
            print("Herzlichen Glückwunsch, du hast das Wort erraten!")
        
    else:
        print("Der Buchstabe", buchstabe, "befindet sich nicht im Wort")
        n -= 1
        print("Anzahl der verbleibenden Versuche:", n)
        print("Neuer Versuch!")
        
if n == 0:
    print("Leider hast du alle Versuche verbraucht, du Idiot. Das Wort war", wort)
elif n < 0:
    print("Also ich bitte dich, < 0 Versuche ist schon lächerlich. Das Wort war", wort)