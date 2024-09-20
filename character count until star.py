upper_count = 0
lower_count = 0
digit_count = 0

while True:
    ch = input("Enter a character: ")
    if ch == '*':
        break
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        digit_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Numbers:", digit_count)
