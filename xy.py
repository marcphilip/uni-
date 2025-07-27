x = "Informatik 2023"
'''
print(x[4])
print(x[5:10])
print(x[0:5])
print(x[9:5:-1])
'''

word1 = input("Enter a word to test for palindorme ")
word1 = word1.lower().replace(" ", "")

word1_backwards = word1[::-1]

if (word1 == word1_backwards):
    print("Palindrome")
else:
    print("Not a palindrome")