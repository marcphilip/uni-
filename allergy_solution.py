# list of food
food_list = [["pizza", "flour", "meat", "olives", "salt"],
             ["burger", "flour", "meat"],
             ["soup", "lentils", "spices", "meat"],
             ["bread", "flour", "yeast", "salt", "sugar"],
             ["salad", "spinach", "yoghurt", "milk"]]

allergens = ["butter", "flour",  "meat"]  # List of allergen

'''
# Your comparision Logic here:
# Loesungsvorschlag
# Bitte beachten Sie die genaue ablauf des Programms
for food in food_list:
    allergen_found = False
    for allergen in allergens:
        if (allergen in food):
            print("You cannot eat", food[0], "because of", allergen)
            allergen_found = True
        if (allergen_found):
            break
    if (not allergen_found):
        print("You can eat", food[0])
'''

# idee 3
allergen_set = set(allergens)
for foods in food_list:
    my_food = foods[0]
    food_set = set(foods)
    common = food_set.intersection(allergen_set)
    if (len(common) > 0):
        print("Allergens found on ", my_food, common)
    else: 
        print("You can eat", my_food)
