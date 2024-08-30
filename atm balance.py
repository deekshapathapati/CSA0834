total_balance = 0

for _ in range(4):
    denomination = int(input("Enter Denomination: "))
    num_notes = int(input("Enter number of notes: "))
    total_balance += denomination * num_notes

print("Total available balance:", total_balance)
