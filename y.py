# athor Marc Philip Zimmermann
# version 1.0 19.04.2023

#input data 
color = input("What's your favorite color? ")
color = color.lower()
color = color.strip()
name = "" 
'''Dient zum Vermeidung von Abstürzung! Denn der Name wurde nur bei der Farbe "red" definiert. 
Sollte man dann aber mal "green" eingeben kommt ja kein Name raus. 
Ich habe den Namen ja nur für red definiert. Das bedeutet dann, dass das ganze Programm nicht funktioniert.
Mit diesen Anführungszeichen wird dann einfach schonmal etwas definiert, damit dann, wenn man beispielsweise "Green" eingibt
dann einfach nur "" rauskommt'''

if(color=="red"):
    print("That's the color of love. Great choice")
    name = "Marc"
elif(color=="blue"):
    print("That's the color of the sky. Great choice")
elif(color=="green"):
    print("That's the color of the gras. Great choice")
else:
    color = color.title()
    print("Nice, great choise. I don't know the color", color, "yet!")

print(color)
print(name)
