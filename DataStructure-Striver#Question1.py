def zeroMatrix(matrix):
    check_col = False
    check_row = False

    # check for column having zeros
    for i in range(0,len(matrix[0])):
        if (matrix[i][0]==0):
            check_col=True

    for i in range(0,len(matrix[0])):
        if matrix[0][i]==0:
            check_row = True

    # check for rest of zeros mark the row and columns using first row and column
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if (matrix[i][j]==0):
                matrix[0][j]=0
                matrix[i][0]=0

    # zerofy the marked columns and rows
    for i in range(1,len(matrix)):
        if (matrix[i][0]==0):
            for j in range(1,len(matrix[0])):
                matrix[i][j]=0

    for i in range(1,len(matrix)):
        if matrix[0][i]==0:
            for j in range(1,len(matrix)):
                matrix[i][j]=0

    if check_col:
        for i in range(0,len(matrix)):
            matrix[i][0]=0

    if check_row:
        for i in range(0,len(matrix[0])):
            matrix[0][i]=0

    return matrix

if __name__ == "__main__":
	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	ans = zeroMatrix(matrix)

	print("The Final matrix is:")
	for row in ans:
		for ele in row:
			print(ele, end=" ")
		print()

