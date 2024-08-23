vehicle_type = input("Enter the type of vehicle (c for car, b for bus, t for truck, y for cycle/bike): ")
hours = int(input("Enter the number of hours: "))

if vehicle_type in ['b', 't']:
    charge = 20 * hours
elif vehicle_type == 'c':
    charge = 10 * hours
elif vehicle_type in ['y']:
    charge = 5 * hours
else:
    charge = 0

print(f"Total parking charge: ₹{charge}")
