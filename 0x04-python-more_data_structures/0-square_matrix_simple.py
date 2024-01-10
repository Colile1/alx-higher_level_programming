#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r_matrix = [[0 for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            r_matrix[i][j] = matrix[i][j] ** 2

    return (r_matrix)
