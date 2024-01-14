"""
-------------------------------------------------------
Test 6 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import is_valid
if __name__ == "__main__":
    # Test cases
    test_names = ["variable", "_underscore", "123variable", "my_var2", "$invalid", "", "123", "variable-name"]
    
    for name in test_names:
        result = is_valid(name)
        print(f"{name} is a valid Python variable name: {result}")
