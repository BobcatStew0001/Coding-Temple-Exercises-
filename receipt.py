item1_name = "Notebook"
item1_price = float("4.99") #This was a string but because it deals with money I made it a float to include the decimal
item1_qty = int("2") #This was a string as well but needed to be cast as an int to get the qty of the item. 
item1_total = item1_price * item1_qty



item2_name = "Pen Pack"
item2_price = float("7.50") #I did the same on line 9 and 10 as 2 and 3 for the same reason mentioned above. 
item2_qty = int("1")
item2_total = item2_price * item2_qty

item3_name = "Backpack"
item3_price = float("34.99") #I also had to repeat it on these lines 
item3_qty = int("1")
item3_total = item3_price * item3_qty

subtotal = item1_total + item2_total + item3_total

tax_rate = float("0.075") #7.5% sales tax
tax_total = subtotal * tax_rate

total = subtotal + tax_total



border = "=" * 30 #This is where I used the str multiplication trick. I never knew about it and wonder is it something similar in C#?
divder = "-" * 30 #It's a pretty neat trick. 

print(border)
print("  The Shop Around the Corner")
print(border)

print(f"{item1_name}    ${item1_price:.2f} x {item1_qty}    ${item1_total:.2f}") #I added $ and :.2f to all the money values. 
print(f"{item2_name}    ${item2_price:.2f} x {item2_qty}    ${item2_total:.2f}")
print(f"{item3_name}   ${item3_price:.2f} x {item3_qty}   ${item3_total:.2f}")# Alignment was tricky & took some trial & error

print(divder)
print(f"Subtotal:               ${subtotal:.2f}")
print(f"Tax (7.5%):              ${tax_total:.2f}")
print(divder)
print(f"Total:                  ${total:.2f}")