arr = list(map(int, input("Enter the sorted array: ").split()))

result = []
for num in arr:
    if num not in result:
        result.append(num)

print("Array after removing duplicates:", result)
