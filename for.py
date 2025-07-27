# for schleife
# marc philip zimmermann

for variable in range(10):
    print("Hello World". variable)

# hier würde jetzt 10 mal Hello World und die Zahlen von 1 bsi 10 geprintet werden!

for _ in range(10):
    print("Hello World")

# _ bedeutet, dass man mit der Variable _ nichts macht. Es würde also nur Hello World rauskommen


for x in range(2, 10):
    print(x)

# hier werden die Zahlen von 1 bis 9 rauskommen

for x in range(2, 10, 2):
    print(x)

# hier werden die Zahlen in zweier schritten ausgegeben


for x in range(10):
    print(x)
    print("Hello World")

#Interation/Wiederholung

zaehler=25
nenner=5
counter=0

while(zaehler >= 0):
    zaehler=zaehler-nenner
    counter += 1 
print("The answer is", counter)


zahl1=4
zahl2=6
sum=0

for i in range(zahl2):
    sum= sum+zahl1

print("The answer of this multiplication", sum)


