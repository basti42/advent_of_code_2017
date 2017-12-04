#!/usr/bin/env python3

import sys

"""
Advent of Code - Day 1:
    Part 1 --> SOLVED
    Part 2 --> SOLVED
"""

def sum_of_matches(numbers):
    """calculate the sum of all numbers that match the next"""
    matches = 0
    for i,n in enumerate(numbers):
        if n == numbers[i-1]:
            matches += int(n)
    return matches

def sum_of_matches_half_around(numbers):
    """Part 2 of the puzzle, calculate the sum of numbers that match the number half way through the sequence"""
    matches = 0
    # making indices for accessing the number at the position
    step = int(len(numbers)/2)
    for i,n in enumerate(numbers):
        if n == numbers[(i+step)%len(numbers)]:
            matches += int(n)
    return matches


# Start the program with the sequence of numbers
# as a command line argument in sys.argv[1]

if __name__ == "__main__":
    numbers = sys.argv[1]
    print("Length of the input: {}".format(len(numbers)))
    matches = sum_of_matches(numbers)
    print("Sum of all numbers that match the next: {}".format(matches))

    half_way_matches = sum_of_matches_half_around(numbers)
    print("Sum of all numbers that match the half-way-round-number: {}".format(half_way_matches))

