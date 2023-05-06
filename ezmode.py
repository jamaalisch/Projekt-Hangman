from getpass import getpass
import re

n = 7
wort_erraten = False
geratene_buchstaben = []


def hang(n):
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


wort = getpass("Gib ein beliebiges Wort an, welches mehrere Buchstaben hat: \n").lower()


if re.findall('\d+', wort):
    print("Welches Wort beinhaltet denn bitte Zahlen? \nDu Idiot. \nVersuche es noch einmal ohne Zahlen!")
    exit()

wort_liste = list(wort)
wort_leerstellenliste = ["_" for i in range(len(wort))]
print("Anzahl der verbleibenden Versuche:", n)
print("Das Wort hat", len(wort), "Buchstaben.")


while n > 0 and not wort_erraten:
    print("_____________Another One_____________")
    print("Du hast diese Buchstaben bereits geraten:\n", *geratene_buchstaben)
    buchstabe = input("Gib einen Buchstaben an, welchen du im Wort vermutest: \n")[0].lower()

    if buchstabe in geratene_buchstaben:
        print("Du hast diesen Buchstaben bereits geraten. Du bekommst für deine Dummheit 1 Versuch abgezogen.")
        n -= 1
        print("Anzahl der verbleibenden Versuche:", n)

    geratene_buchstaben.append(buchstabe)

    if buchstabe in wort_liste:
        print("Der Buchstabe", buchstabe, "befindet sich im Wort.")

        for i in range(len(wort)):
            if wort_liste[i] == buchstabe:
                wort_leerstellenliste[i] = buchstabe
        print(" ".join(wort_leerstellenliste))

        if "_" not in wort_leerstellenliste:
            wort_erraten = True
            print("Herzlichen Glückwunsch, du hast das Wort erraten!")
        
    else:
        print("Der Buchstabe", buchstabe, "befindet sich nicht im Wort")
        n -= 1
        print("Anzahl der verbleibenden Versuche:", n)
        print("Neuer Versuch!")
    hang(n)
    
if n == 0:
    print("Leider hast du alle Versuche verbraucht, du Idiot. Das Wort war", wort)
elif n < 0:
    print("Also ich bitte dich, < 0 Versuche ist schon lächerlich. Das Wort war", wort)
