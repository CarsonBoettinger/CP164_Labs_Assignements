"""
-------------------------------------------------------
Test 7 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import max_diff
if __name__ == "__main__":
    test_list = [40, 20, 10, 5]
    test_list2=[40,2,40,3,45,67]
    result = max_diff(test_list)
    result2= max_diff(test_list2)
    print(f"The maximum absolute difference in the list is: {result} and {result2}")