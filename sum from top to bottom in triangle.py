triangle = [
    [3],
    [4, 6],
    [2, 7, 6],
    [8, 5, 9, 3]
]

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

print("The maximum total from top to bottom is:", triangle[0][0])
