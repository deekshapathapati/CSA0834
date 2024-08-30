array = list(map(int, input("Enter numbers separated by space: ").split()))
M = int(input("Enter Mth maximum: "))
N = int(input("Enter Nth minimum: "))

sorted_array = sorted(array)
Mth_max = sorted_array[-M]
Nth_min = sorted_array[N-1]

print("Sum:", Mth_max + Nth_min)
print("Difference:", Mth_max - Nth_min)
