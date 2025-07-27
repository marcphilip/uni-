# author Marc Philip Zimmermann
# Version 1.1


#input data
name = input("Hallo, wie heißt du? ")
note = input("Wie viele Punkte hast du in der Klausur bekommen (von 100)? ")
note = float(note)

# outputs by using the if-method 
if(note < 16):
    print("Tut mir leid",name.title(),", du hast leider eine 6... :(")

elif(note < 45):
    print("Schade..",name.title(),", du hast leider eine 5...")

elif(note < 60):
    print("Ohje..",name.title(),", du hast eine 4...")

elif(note < 80):
    print("Immerhin",name.title(),", du hast die Hälfte richtig und eine 3")

elif(note < 96):
    print("Sehr gut",name.title(),", du hast eine 2")

else: 
    print("Wow",name.title(),", hast eine 1! Sehr gut!:)")


