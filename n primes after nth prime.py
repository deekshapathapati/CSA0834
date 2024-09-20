def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the value of n: "))
count = 0
num = 2
primes = []

while count < n:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1

count = 0
while count < n:
    if is_prime(num):
        print(num)
        count += 1
    num += 1
