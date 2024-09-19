num = int(input("Enter a number: "))
num_str = str(num)
length = len(num_str)

if length%2 == 0:
    first_half = int(num_str[:length//2])
    second_half = int(num_str[length//2:])
    sum_of_parts = first_half + second_half
    
    if sum_of_parts ** 2 == num:
        print(f"{num} is a Tech Number.")
    else:
        print(f"{num} is not a Tech Number.")
else:
    print(f"{num} is not a Tech Number.")
