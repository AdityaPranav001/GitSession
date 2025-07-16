def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n - 1 - i]
    
    return abs(primary_diagonal_sum - secondary_diagonal_sum)


print(diagonalDifference([  [1,2,3],
                            [4,5,6],
                            [7,8,9]  ]))