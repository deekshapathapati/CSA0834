from math import gcd

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

lcm = numbers[0]
for i in numbers[1:]:
    lcm = lcm * i // gcd(lcm, i)

gcd_result = numbers[0]
for i in numbers[1:]:
    gcd_result = gcd(gcd_result, i)

print("LCM:", lcm)
print("GCD:", gcd_result)
