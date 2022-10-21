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
          medianform = numbers.size()+1
          if medianform%2==0:
             med = numbers[(numbers.size()/2)-1]
          else:
              med = (numbers[(numbers.size()/2)-1] + numbers[numbers.size()/2])/2       

        break
print(med)
