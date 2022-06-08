def diagonalDifference(arr):
    n =len(arr)
    diagonal1 = 0
    diagonal2 = 0
    for e in range(0, n):
        diagonal1 = diagonal1 + arr[e][e]
        diagonal2 = diagonal2 + arr[n-e-1][e]

    return diagonal2-diagonal1 if diagonal2-diagonal1>0 else diagonal1-diagonal2

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, (-12)]]))
