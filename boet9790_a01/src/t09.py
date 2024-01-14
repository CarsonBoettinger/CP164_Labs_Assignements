"""
-------------------------------------------------------
Test 9 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import matrixes_add
if __name__ == "__main__":
    matrix_a = [[0, 1], [2, 3], [4, 5]]
    matrix_b = [[6, 7], [8, 9], [1, 0]]

    result_matrix = matrixes_add(matrix_a, matrix_b)
    for row in result_matrix:
        print(row)