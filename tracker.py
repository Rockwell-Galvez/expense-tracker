# Talking to the User | Installment 2 Author: Rockwell Galvez
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
item1 = input("\nWhat is first expense? ")
amount1 = float(input(f"What is the amount for {item1}? "))
item2 = input("What is second expense? ")
amount2 = float(input(f"What is the amount for {item2}? "))

total = amount1 + amount2
average = total / 2
print("-" * 40)
print("SUMMARY")
print(f" - {item1}: \t\t₱{amount1}")
print(f" - {item2}: \t\t₱{amount2}")
print(f"Total expense: \t\t₱{total}")
print(f"Average expense: \t₱{average}")

print("-" * 40)
print("Made by: Rockwell Galvez | Installment 2")