#This program takes a list and lets a user add and remove items from the list.


my_list = ["Pick up groceries", "Fill the truck with gas", "Buy my wife's b-day gift"]

print("=" * 35)
print("       My To-Do List")
print("=" * 35)

for i, todo in enumerate(my_list, start=1): # 1st printing of the list.
    print(f"{i}. {todo}")


new_errand = input("Add to my list: ").strip() #I removed the Try/Except here it was dead code after I used the if/else
if new_errand == "" or new_errand.isdigit():
    print("That's not a valid task, adding Buy Banana's instead")#Tells them that it is a invalid input and that we are adding buy bananas
    my_list.append("Buy Banana's")
else:
    my_list.append(new_errand)

for i, todo in enumerate(my_list, start=1): #Revised list printing
    print(f"{i}. {todo}")


try:
    check_off = int(input("Check a task off the list: ")) # I moved this into the try block so the try would catch the errors.
    if (check_off < 1 or check_off > len(my_list)): # The if statement checks if the input is in the list range
        print("That's not a valid task!") #This prevents an IndexError
    else:
        removed = my_list.pop(check_off - 1) # I added the -1 and removed the line int(check_off)-1
        print(f"Done with this {removed}")
except ValueError:  # This catches if the user enters a non-integer
    print("That's not a valid number")
for i, todo in enumerate(my_list, start=1): # Revised list printing
    print(f"{i}. {todo}")

print(f"I have {len(my_list)} tasks") #List count

