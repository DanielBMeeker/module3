"""
Program: Basic input and output
Author: Daniel Meeker
Date: 06/05/2020

This program will demonstrate getting input
from the user and formatting the output back
to the user while keeping test driven development
in mind.
"""


def average():
    # Get user input for scores
    score1 = input("Please enter a value for score 1: ")
    score2 = input("Please enter a value for score 2: ")
    score3 = input("Please enter a value for score 3: ")
    # Calculate and return average
    return (float(score1)+float(score2)+float(score3))/3


# Get user information
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
age = input("Please enter your age: ")
average_scores = average()
# Format output and print to console
print('{}, {} age: {} average grade: {:.2f}'.format(last_name, first_name, age, average_scores))


