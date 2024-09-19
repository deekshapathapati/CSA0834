n = int(input("Enter the size of the matrix (n x n): "))
matrix = []

for _ in range(n):
    row = list(map(int, input("Enter row elements separated by spaces: ").split()))
    matrix.append(row)

main_diagonal_sum = 0
secondary_diagonal_sum = 0

print("Main Diagonal:")
for i in range(n):
    print(matrix[i][i], end=' ')
    main_diagonal_sum += matrix[i][i]
print()

print("Secondary Diagonal:")
for i in range(n):
    print(matrix[i][n-1-i], end=' ')
    secondary_diagonal_sum += matrix[i][n-1-i]
print()

print("Sum of Main Diagonal:", main_diagonal_sum)
print("Sum of Secondary Diagonal:", secondary_diagonal_sum)
