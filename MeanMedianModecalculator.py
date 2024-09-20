import statistics

arr = list(map(int, input("Enter the array of numbers: ").split()))

mean = sum(arr) / len(arr)
median = statistics.median(arr)
mode = statistics.mode(arr)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
