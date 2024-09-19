arr = list(map(int, input("Enter sorted array elements separated by spaces: ").split()))
target = int(input("Enter the target value: "))

start, end = -1, -1

for i in range(len(arr)):
    if arr[i] == target:
        start = i
        break

if start != -1:
    for i in range(start, len(arr)):
        if arr[i] == target:
            end = i
        else:
            break

print("Starting and ending positions:", [start, end])
