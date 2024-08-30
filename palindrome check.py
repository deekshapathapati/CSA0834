choice = input("Choose case (1 for string, 2 for number): ")

if choice == "1":
    string = input("Enter a string: ")
    if string == string[::-1]:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")
elif choice == "2":
    number = input("Enter a number: ")
    if number == number[::-1]:
        print("Number is a palindrome")
    else:
        print("Number is not a palindrome")
