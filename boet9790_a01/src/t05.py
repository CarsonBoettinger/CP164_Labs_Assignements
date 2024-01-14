"""
-------------------------------------------------------
Test 5 Assignment 1 
-------------------------------------------------------
Author:  Carson Boettinger
ID:      210799790
Email:   boet9790@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import is_leap_year
if __name__ == "__main__":
    # Test cases
    test_years = [1996, 2000, 2004, 1899, 1900, 1901, 1700, 1800, 1900, 1600, 2000]
    
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year} is a leap year: {result}")