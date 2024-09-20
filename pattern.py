char = input("Enter the Character to be printed: ")
n = int(input("Max Number of time printed: "))

for i in range(1, n + 1):
    print((char + " ") * i)
