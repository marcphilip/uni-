# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
import random
my_choice = random.randint(1,20)
print(my_choice)
chances = 5

while(chances > 0):
    user_choise = int(input("Enter your guess: "))
    if( user_choise > my_choice):
        print("lower")
        chances = chances - 1
    elif( user_choise < my_choice):
        print("higher")
        chances = chances - 1
    else:
        print("Jackpot")
        break