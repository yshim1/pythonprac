#Intro
"""
A matrix is a 2-dimensional array. Questions involving matrices are usually related to dynamic programming
or graph traversal. Matrices can be used to represent graphs where each noce is a cell on the matrix
which has 4 neighbors (except edge and corner cells)"""

#Corner cases
"""
Empty matrix. Check that none of the arrays are 0 length
1x1 Matrix
Matrix with only one row or column
"""

#Techniques
"""
Creating an empty NxM matrix
For questions involving traversal or dynamic programming, you almost always want to make a copy of the matrix with the
same size/dimensions that is initialized to empty values to store the visited state or dynamic programming table."""

matrix = [[1,2,3], [4,5,6], [7,8,9]]
#assumes that the matrix is non-empty
zero_matrix = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]
#copying a matrix in python is
copied_matrix = [row[:]for row in matrix]

"""
Transposing a  matrix
The transpose of a matrix is found by interchanging its rows into columns or columns into rows
Many grid-based games can be modeled as a matrix, such as Tic-Tac-Toe, Sudoku, Crossword, Connect 4, 
Battleship, etc. It is not uncommon to be asked to verify the winning condition of the game. For games 
like Tic-Tac-Toe, Connect 4 and Crosswords, where verification has to be done vertically and horizontally, 
one trick is to write code to verify the matrix for the horizontal cells, transpose the matrix, and reuse 
the logic for horizontal verification to verify originally vertical cells (which are now horizontal).
"""
transposed_matrix = map(list, zip(*matrix))

print(zero_matrix)
print(copied_matrix)
print(list(transposed_matrix))