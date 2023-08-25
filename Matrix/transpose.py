def transpose(A):
    N=len(A)
    for i in range(N):
        for j in range(i+1, N):
            A[i][j], A[j][i] = A[j][i], A[i][j]
        print(A)
    


# driver code
A = [[1, 1, 1, 1],
	[2, 2, 2, 2],
	[3, 3, 3, 3],
	[4, 4, 4, 4]]

transpose(A)
print(A)