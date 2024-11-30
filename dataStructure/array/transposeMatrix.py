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
    # transpose = [[0]* rowsCount]*colsCount Incorrect, why?
    # Instead of creating independent copies, Python creates multiple references to the same list in memory.
    # changing one row changes all of them !!

    # ensure each row is independent, you need to create a new list for each row
    transpose = [[0]* rowsCount for _ in range(colsCount)]

    for row in range(rowsCount):
        for col in range(colsCount):
            transpose[col][row] = matrix[row][col] 
    return transpose
