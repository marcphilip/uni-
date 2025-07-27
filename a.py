# author marc philip zimmermann
# version 1.0

'1-15 unter aufsicht / nicht - darf nicth trinken'
'16-18 unter aufsicht - darf trinken'
'ab 18 unter aufsicht / ohne - darf trinken'

age = int(input("How old are you? "))
begleitperson = input("is there any companion?(y/n) ") # y/n stands for yes or no and is a command to only type yes or no
if (begleitperson.strip().lower() == 'y'):
    begleitperson = True
else:
    begleitperson = False

if( age < 16):
    print("You are not allowed to drink!")
elif (age < 18 and begleitperson): 
    print("You are  allowed to drink!")
elif (age < 18 and not begleitperson ): #ich hätte auch:(age >= 16 and age < 18 and begleitperson == False): schreiben können!
    print("You are not allowed to drink ")
else:
    print("You are allowed to drink!")
