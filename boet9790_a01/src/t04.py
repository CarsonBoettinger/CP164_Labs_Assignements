"""
-------------------------------------------------------
Test 4 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""

from functions import file_analyze
if __name__ == "__main__":
    # Open a file for testing
    with open('test_file.txt', 'w') as test_file:
        test_file.write("Hello World!\n123 Test 456\n   whitespace   ")

    # Open the file for reading and analyze it
    with open('test_file.txt', 'r') as file_to_analyze:
        upp, low, dig, whi, rem = file_analyze(file_to_analyze)

        print("Uppercase letters:", upp)
        print("Lowercase letters:", low)
        print("Digits:", dig)
        print("Whitespace characters:", whi)
        print("Remaining characters:", rem)