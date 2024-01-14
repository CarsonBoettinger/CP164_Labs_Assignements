"""
-------------------------------------------------------
Test 2 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import list_subtraction

if __name__ == "__main__":
    minuend = [5, 5, 4, 5]
    subtrahend = [5]
    
    print("Original Minuend:", minuend)
    print("Subtrahend:", subtrahend)
    
    list_subtraction(minuend, subtrahend)
    
    print("Modified Minuend:", minuend)
