# The Tracker Makes Decisions | Installment 4 | Author: Rockwell Galvez
print( "=" * 40)
print("\t     EXPENSE TRACKER")
print("\tWhere Numbers Make Sense.")
print( "=" * 40)
print("\nMAIN MENU")
print("  [1] Add an expense   \t\t(coming soon)")
print("  [2] View all expenses\t\t(coming soon)")
print("  [3] Show total spent \t\t(coming soon)")
print("  [4] Exit             \t\t(coming soon)\n")

name = input("What is your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("\nWhat is first expense? ")
amount1 = float(input(f"What is the amount for {item1}? "))

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print(  "Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("What is second expense? ")
amount2 = float(input(f"What is the amount for {item2}? "))

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print(  "Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two Big Expenses in a row - Slow Down")

tax_percent = float(input(f"What is the Tax rate %? "))
budget = float(input(f"What is the Budget? "))


subtotal = amount1 + amount2
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = tax + subtotal
over_budget = total > budget
left = budget - total

print(f"\n{'-' * 40}")
print("SUMMARY")
print(f"  - {item1}:\t\t${amount1}")
print(f"  - {item2}:\t\t${amount2}")
print(f"Subtotal expense:\t${subtotal}")
print(f"Average expense:\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand Total expense:\t${total}")
if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")


print("-" * 40)
print("Made by: Rockwell Galvez | Installment 4")