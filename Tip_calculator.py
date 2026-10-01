print("--- Tip Calculator---")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15, or 20? "))

# Calculate the Final amount
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount

print(f"Your tip is ${tip_amount:.2f}")
print(f"Your total bill is ${total_amount:.2f}")