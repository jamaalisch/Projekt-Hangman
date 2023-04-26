import zufallsworte as zufall
import random

n = 7                                                                                                                                                      # Versuche des Spielers, bis dieser verloren hat
wort_erraten = False                                                                                                                                        # Angabe, ob das Wort erraten wurde
geratene_buchstaben = []                                                                                                                                    # leere Liste für Buchstaben, die schon erraten wurden
wort = zufall.anzahl_buchstaben(random.randint(3, 28), 1)                                                                                                   # Eins von 300k Wörtern wird zufällig ausgewählt. Die Länge ist auch zufällig
wort_liste = [buchstabe.lower() for buchstabe in wort[0]]                                                                                                   # Eine Liste mit allen Buchstaben des Worts wird erstellt
wort_leerstellenliste = ["_" for i in range(len(wort_liste))]                                                                                               # Anhand von der Anzahl der Buchstaben wird bestimmt, wie viele leere Striche kreiert werden müssen
print("Anzahl der verbleibenden Versuche:", n)                                                                                                              # Ausgabe Anzahl Fehlversuche
print("Das Wort hat", len(wort_liste), "Buchstaben.")

def einetollegrafischedarstellungfürherrhergaßweilerdaraufbestehtundersonstimlebennichtglücklichwerdenkann (n):                                             # steht da was es ist lol
        
    if n == 7:
        print("_______\n|/\n|\n|\n|\n|\n----------")
    elif n == 6:
        print("_______\n|/  |\n|\n|\n|\n|\n----------")
    elif n == 5:
        print("_______\n|/  |\n|   O\n|\n|\n|\n----------")
    elif n == 4:
        print("_______\n|/  |\n|   O\n|   | \n|\n|\n----------")  
    elif n == 3:
        print("_______\n|/  |\n|   O\n|  /| \n|\n|\n----------")
    elif n == 2:
        print("_______\n|/  |\n|   O\n|  /|\ \n|\n|\n----------")
    elif n == 1:
        print("_______\n|/  |\n|   O\n|  /|\ \n|  / \n----------") 
    elif n == 0:
        print("_______\n|/  |\n|   O\n|  /|\ \n|  / \ \n----------")

while n > 0 and not wort_erraten:
    print("_____________Another One_____________")
    print("Du hast diese Buchstaben bereits geraten:\n",*geratene_buchstaben)  
    buchstabe = input("Gib einen Buchstaben an, welchen du im Wort vermutest: \n")[0].lower()                                                               # Eingabe eines! Buchstabens. Wird mit .lower() kleingemacht, damit es keine Probleme gibt

    if buchstabe in geratene_buchstaben:                                                                                                                    # Überprüfung, ob ein Buchstabe bereits geraten wurde
        print("Du hast diesen Buchstaben bereits geraten, du Idiot. Haste jetzt verloren. Hättest du mal vorher überlegt wa?")
        n -= n

    geratene_buchstaben.append(buchstabe)																													# Hinzufügen des geratenen Buchstabens zur Liste

    if buchstabe in wort_liste:                                                                                                                             # Überprüfung, ob der Buchstabe im Wort vorhanden ist
        print("Der Buchstabe", buchstabe, "befindet sich im Wort.")

        for i in range(len(wort_liste)):                                                                                                                    # Schleife über alle Buchstaben des Worts
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
    einetollegrafischedarstellungfürherrhergaßweilerdaraufbestehtundersonstimlebennichtglücklichwerdenkann(n)
if n == 0:
    print("Leider hast du alle Versuche verbraucht, du Idiot. Das Wort war", wort)
elif n < 0:
    print("Also ich bitte dich, < 0 Versuche ist schon lächerlich. Das Wort war", wort)