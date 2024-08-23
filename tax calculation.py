income = float(input("Enter your taxable income: "))

if income <= 150000:
    tax = 0
elif income <= 300000:
    tax = 0.10 * (income - 150000)
elif income <= 500000:
    tax = 0.10 * 150000 + 0.20 * (income - 300000)
else:
    tax = 0.10 * 150000 + 0.20 * 200000 + 0.30 * (income - 500000)

print(f"The tax to be paid is: ₹{tax:.2f}")
