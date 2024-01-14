"""
-------------------------------------------------------
Test 1 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""

from functions import clean_list

if __name__ == "__main__":
    values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4, 3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]
    print("Original List:", values)
    clean_list(values)
    print("Cleaned List:", values)
