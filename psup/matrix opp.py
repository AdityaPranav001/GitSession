def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))

# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Perform operations
print("Addition of A and B:")
print(add_matrices(A, B))

print("\nSubtraction of B from A:")
print(subtract_matrices(A, B))

print("\nMultiplication of A and B:")
print(multiply_matrices(A, B))

print("\nTranspose of A:")
print(transpose_matrix(A))

print("\nDiagonal sum of A:", diagonal_sum(A))
print("Diagonal sum of B:", diagonal_sum(B))
