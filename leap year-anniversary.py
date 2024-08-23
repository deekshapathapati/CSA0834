def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter Year: "))

if is_leap_year(year):
    print(f"Given Year: Leap Year.")
    print(f"Next Anniversary Year: {year + 1}")
else:
    print(f"Given Year: Non Leap Year.")
    print(f"Previous Anniversary Year: {year - 1}")

