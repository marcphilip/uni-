#author marc 
#version 1.0
''''
for number in range(1,21):
    if(number % 3 == 0 and number % 5 == 0):
        print("Fizz Buzz")
    elif(number % 5 == 0):
        print("Buzz")
    elif(number % 3 == 0):
        print("Fizz")
    else:
        print(number)
'''

for number in range(1,21):
    message = ""
    if( number % 3 == 0 ):
        message = "Fizz "
    if( number % 5 == 0 ):
        message = message + "Buzz "
    
    print(number if message == "" else message)    


''''if(message == ""):
        print(number)
    else:
        print(number)'''