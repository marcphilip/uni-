'''
Wir haben in unserem Treffen ein kleines Ratespiel in Python programmiert.
Das Problem bestand darin, dass die vom Computer "gedachte" Zahl immer gleich war.
Jetzt möchtest du es aufregender gestalten! Passe das Programm so an, dass während
der Laufzeit eine Zufallszahl generiert wird. 

Für noch mehr Spannung (Bonus): Dem Benutzer stehen nur 5 Versuche zur Verfügung,
um die Zahl zu erraten.
Tipp 1: Benutze "random" für die Generieung von Zufallszahl.
https://www.programiz.com/python-programming/examples/random-number

Tipp 2: Um die "Chancen" zu implementieren, erstelle eine Variable die immer
hochzählt wenn eine "falsche" nummer geraten wird. Was musst du da noch ändern? ;)
'''


import random
random_number = random.randint(1,20)
print(random_number)
should_run = True
tries = 1

while(should_run):

    user_input = int(input("Enter you guess? "))
    if(tries == 5):
        print("You failed to guess the number. The number was", random_number)
        should_run = False
    elif (user_input == random_number):
        print("Correct! You have the number", random_number)
        should_run = False
    elif (user_input < random_number):
        print("Not correct, you should go higher!")
        tries = tries + 1
    else:
        print("Not correct, you should go lower")
        tries = tries + 1
