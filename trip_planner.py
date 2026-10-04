destination = input("Where would you like to go? ")

distance = float(input("What's the total distance in miles? "))

car_mpg = float(input("What's your car's fuel economy (mpg)? ")) #I am tring to get better with the names for my variables. It has been weak point

gas_price = float(input("What's the price of gas per gallon? "))

trip_length = int(input("How many nights are you staying? "))

hotel_per_night = float(input("What's the average cost of a hotel per night? ")) 

food_cost = float(input("How much are you budgeting for food daily? "))

gas_needed = distance / car_mpg

gas_expense = gas_needed * gas_price

hotel_expense = trip_length * hotel_per_night

food_days = trip_length + 1 #one more day of food than nights

food_expense = food_days * food_cost

total_expense = gas_expense + hotel_expense + food_expense

divider = "-" * 29

print()
print("=== Road Trip Budget Planner ===")
print()
print(f"Destination: {destination}")
print(f"Distance: {distance:.2f} miles")
print()

print("--- Cost Breakdown ---")
#:<31 pads each label out to 31 characters so the dollar amounts line up no matter what numbers are entered
print(f"{f'Gas ({gas_needed:.2f} gal @ ${gas_price:.2f}/gal):':<31}${gas_expense:.2f}")
print(f"{f'Hotel ({trip_length} nights @ ${hotel_per_night:.2f}):':<31}${hotel_expense:.2f}")
print(f"{f'Food ({food_days} days @ ${food_cost:.2f}):':<31}${food_expense:.2f}")

print(divider)

print(f"{'Estimated Total:':<31}${total_expense:.2f}")
