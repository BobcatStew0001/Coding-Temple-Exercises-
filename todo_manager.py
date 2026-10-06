#This program takes a list and lets a user add and remove items from the list.

my_list = ["Pick up groceries", "Fill the truck with gas", "Buy my wife's b-day gift"]

print("=" * 35)
print("       My To-Do List")
print("=" * 35)

for i, todo in enumerate(my_list, start=1): # 1st printing of the list.
    print(f"{i}. {todo}")

try:
    new_errand = input("Add to my list: ")

except ValueError:
    print("Invalid input! Use buy banana's")
    new_errand = "buy banana's"

my_list.append(new_errand) # Adds the user input to the end of the list or adds buy banana's to prevent a crash

for i, todo in enumerate(my_list, start=1): #Revised list printing
    print(f"{i}. {todo}")

check_off = int(input("Check a task off the list: "))
try:
    int(check_off) - 1
    removed = my_list.pop(check_off)
    print(f"Done with this {removed}")
except ValueError:  # This catches if the user enters a non-integer
    print("That's not a valid number")
except IndexError: # This catches if the number entered is not in the list.
    print("The number isn't on the list")

for i, todo in enumerate(my_list, start=1): # Revised list printing
    print(f"{i}. {todo}")

print(f"I have {len(my_list)} tasks") #List count

