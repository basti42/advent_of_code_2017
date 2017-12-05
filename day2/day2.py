#!/usr/bin/env python3

import sys

"""
Advent of Code - Day 2:
    Part 1 --> SOLVED
    Part 2 --> SOLVED
"""

def calc_checksums(rows):
    checksums = []
    # determine the min and max for each row
    # calculate the checksum as difference and append it to the list
    for row in rows:
        maxi, mini = max(row), min(row)
        # print("MAX: {}\tMIN: {}".format(maxi, mini))
        checksums.append(maxi-mini)
    return checksums


def calc_checksums_evens(rows):
    checksums = []
    # determine the min and max for each row
    # calculate the checksum as difference and append it to the list
    for row in rows:
        a,b = find_even(row)
        cs = a/b if a>b else b/a
        checksums.append(int(cs))
    return checksums

def find_even(row):
    a,b = -1, -1
    for n in row:
        for m in row:
            if n == m:
                continue
            else:
                if n%m == 0:
                    a,b = n, m
                    break
        if a != -1:
            break
    return a,b

if __name__ == "__main__":
    with open("testing_inputs/input_2.txt", "r") as inp:
        cont = inp.read()

    # create a list of numbers for each row
    cont = [ [ int(x) for x in row.split(" ") if len(x)>0 ] for row in cont.split("\n")  if len(row)>0 ]

    row_checksums = calc_checksums(cont)
    print("Checksum for the file: {}".format(sum(row_checksums)))

    even_checksums = calc_checksums_evens(cont)
    print("Checksum for evens: {}".format(sum(even_checksums)))







