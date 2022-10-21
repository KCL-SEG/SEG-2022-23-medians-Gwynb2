"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import statistics
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        numbers.sort()
        med = statistics.median(numbers)

        break
print(med)
