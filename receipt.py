item1_name = "Notebook"
item1_price = float("4.99")
item1_qty = int("2")
item1_total = item1_price * item1_qty



item2_name = "Pen Pack"
item2_price = float("7.50") 
item2_qty = int("1")
item2_total = item2_price * item2_qty

item3_name = "Backpack"
item3_price = float("34.99")
item3_qty = int("1")
item3_total = item3_price * item3_qty

subtotal = item1_total + item2_total + item3_total

tax_rate = float("0.075") #7.5% sales tax
tax_total = subtotal * tax_rate

total = subtotal + tax_total



border = "=" * 30
divder = "-" * 30

print(border)
print("  The Shop Around the Corner")
print(border)

print(f"{item1_name}    ${item1_price:.2f} x {item1_qty}    ${item1_total:.2f}")
print(f"{item2_name}    ${item2_price:.2f} x {item2_qty}    ${item2_total:.2f}")
print(f"{item3_name}   ${item3_price:.2f} x {item3_qty}   ${item3_total:.2f}")

print(divder)
print(f"Subtotal:               ${subtotal:.2f}")
print(f"Tax (7.5%):              ${tax_total:.2f}")
print(divder)
print(f"Total:                  ${total:.2f}")