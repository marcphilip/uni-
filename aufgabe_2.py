'''
Schreibe ein Python-Programm, das den Benutzer WIEDERHOLT dazu auffordert, eine Zahl einzugeben.
Wenn die eingegebene Zahl GERADE ist, soll das Programm "Die Zahl ist gerade." ausgeben.
Wenn die eingegebene Zahl UNGERADE ist, soll das Programm "Die Zahl ist ungerade." ausgeben.
Das Programm sollte den Benutzer so lange auffordern, bis er eine NEGATIVE Zahl eingibt.
In diesem Fall soll es z.B. "Programm wird beendet." ausgeben.
Verwende eine while-Schleife und if-Bedingungen, um dieses Verhalten zu implementieren.
Tipp: Benutze den Modulo operator um herauszufinden ob eine Zahl gerade/ungerade ist.
'''

# author marc philip zimmermann
# version 1.0

while(True):

    user_number = int(input("Enter your number to check for odd or even property"))

    if (user_number < 0 ):
        print("The Programm is now terminanted")
        break # Êxit the loop

    elif (user_number % 2 == 0):
        print("It is an even number")

    elif (user_number % 2 != 0):
        print("It is an odd number")