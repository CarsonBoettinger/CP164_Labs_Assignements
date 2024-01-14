"""
-------------------------------------------------------
Test 8 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import matrix_stats
if __name__ == "__main__":
    # Test case
    test_matrix = [
        [4.5, 2.7, 8.1],
        [1.8, 6.3, 5.2],
        [3.4, 7.6, 2.9]
    ]

    small, large, total, average = matrix_stats(test_matrix)

    print(f"Smallest number: {small}")
    print(f"Largest number: {large}")
    print(f"Total of all numbers: {total}")
    print(f"Average of all numbers: {average}")