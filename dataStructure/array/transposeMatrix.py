# give a 2D array of integers (matrix),return the transpose of the matrix.
# Transpose of a Matrix: a filliped version of a matrix across its main diagonal
# Transpose of a matrix is obtained by changing rows to columns and columns to rows.
# matrix = [
#     [1, 2],
#     [3, 4]
# ]

# transposeMatrix = [
#     [1, 3],
#     [2, 4]
# ]

def transposeMatrix(matrix):
    rowsCount = len(matrix)
    colsCount = len(matrix[0])
    transpose = [[0]* rowsCount]*colsCount

    #  fill it with actual values of matrix
    for row in range(rowsCount):
        for col in range(colsCount):
            transpose[col][row] = matrix[row][col] 
    return transpose
