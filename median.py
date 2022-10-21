"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import statistics
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
          numbers.sort()
          med = 0
        break
print(med)
