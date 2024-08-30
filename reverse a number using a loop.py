number = int(input("Enter a number: "))
reversed_number = 0

while number > 0:
    reversed_number = reversed_number * 10 + number % 10
    number //= 10

print("Reversed Number:", reversed_number)
