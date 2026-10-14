# Part 1: Error Detective
# #Snippet 1 Type Error
# #The original code was trying to concat a string and integer. I cast the int to a string to fix it
# print("The answer is: " + str(42))

# #Snippet 2 Type Error
# # The original code was also trying to concat a string and integer. I cast the user input to a int and then in the results variable you can add them together.
# favorite = int(input("Favorite number: "))
# result = favorite + 10
# print(result)

# # Snippet 3 Syntax Error 
# # The original code left out a " at the end of the string. I added that and it fixed the code.
# print("Hello World")

# # Snippet 4 Value Error 
# #The original code had twenty-five instead of 25. You cannot cast twenty-five to an int because it is not a number it is letters . If this was in a program and was taking in user input I was use the try execpt to instruct the user they entered an invalid input and needed to enter a number 
# #age = int("twenty-five")
# # try:
#     #age = int(input("Enter your age in numerical form"))
# #except ValueError: 
#     #print("Your input is invalid, Please try again.")
# age = int("25")

#  # Snippet 5 Name Error 
# #The variable username was called before it was declared. To fix it we need to declare the variable username before it is called.
# username = input("What is your name? ")
# print(username)


#Part 2: Crash-Proof Number Collector

try: number_one = int(input("Enter a number in numeric format"))

except ValueError:
    ("That's not a valid number. Using 0 instead.")
    number_one = 0

try:
    number_two = int(input("Enter a number in numeric format"))

except ValueError:
    ("That's not a valid number. Using 0 instead.")
    number_two = 0

try:
    number_three = int(input("Enter a number in numeric format"))

except ValueError:
    ("That's not a valid number. Using 0 instead.")
    number_three = 0

total = (number_one + number_two + number_three)

print(number_one, number_two, number_three)

print(total)

print(total / 3)
