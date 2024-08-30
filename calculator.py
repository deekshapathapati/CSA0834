x = int(input("Enter x: "))
n = int(input("Enter n: "))
choice = input("Choose operation (pow/add/sub/mul/div): ")

if choice == "pow":
    result = 1
    for _ in range(n):
        result *= x
elif choice == "add":
    result = x + n
elif choice == "sub":
    result = x - n
elif choice == "mul":
    result = x * n
elif choice == "div":
    result = x / n

print("Result:", result)
