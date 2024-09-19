def calculate_fare(distance, time_of_day):
    if distance <= 2:
        fare = 50
    elif distance <= 10:
        fare = 50 + (distance - 2) * 12
    else:
        fare = 50 + (8 * 12) + (distance - 10) * 15
    if (8 <= time_of_day < 10) or (17 <= time_of_day < 20):
        fare *= 1.2
    if distance > 20:
        fare *= 0.9
    if time_of_day >= 23 or time_of_day < 6:
        fare += 100
    return fare
distance = float(input("Enter the distance traveled (in km): "))
time_of_day = int(input("Enter the time of day in 24-hour format (e.g., 14 for 2 PM): "))


total_fare = calculate_fare(distance, time_of_day)

print(f"The total fare is: ₹{total_fare:.2f}")
