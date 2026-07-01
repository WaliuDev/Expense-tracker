expenses = []

for i in range(3):
    amount = float(input(f"Enter expense {i+1}: "))
    expenses.append(amount)

total = sum(expenses)
average = total / len(expenses)

print(f"Total: {total}")
print(f"Average: {average}")

if total > 2000:
    print("Warning: You overspent!")
else:
    print("You are within budget.")
