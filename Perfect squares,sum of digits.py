def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

perfect_squares = [x for x in range(a, b + 1) if (x ** 0.5).is_integer() and sum_of_digits(x) < 10]

print("Perfect squares with sum of digits less than 10:", perfect_squares)
