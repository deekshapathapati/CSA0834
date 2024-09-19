def find_mth_max_nth_min(arr, m, n):
    arr.sort()
    return arr[-m], arr[n-1]

arr = [12, 4, 5, 7, 3, 19, 15]
m = 2
n = 3

mth_max, nth_min = find_mth_max_nth_min(arr, m, n)
print(f"The {m}th maximum number is: {mth_max}")
print(f"The {n}th minimum number is: {nth_min}")
sum = mth_max + nth_min
difference = mth_max - nth_min
print(f"sum is: {sum}")
print(f"difference is: {difference}")
