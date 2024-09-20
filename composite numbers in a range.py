def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

print(f"Composite numbers between {a} and {b} are:")
for num in range(a, b + 1):
    if is_composite(num):
        print(num)
