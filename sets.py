numbers_1 = {1,3,5,7,9}
numbers_3 = {1,3,7,5,9}
numbers_2 = {1,2,3,3,4,5}

# Gleichheit 
print(numbers_1 == numbers_3)

# Operationen
intersection = numbers_1.intersection(numbers_2)
print(intersection)

union = numbers_1.union(numbers_2)

difference = numbers_1.difference(numbers_2)
print(difference)

print(len({}))

x = [1,2,3,4,5,6,6]
x_set= set(x)
print(x_set)

x_list = list(x_set)
print(x_list)

my_word = "mecca"
print(set(my_word))
