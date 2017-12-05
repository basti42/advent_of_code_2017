#!/usr/bin/env python3

import sys

"""
Advent of Code - Day 3
    part 1 --> SOLVED
"""

def find_odd_square(until):
    """find the odd square number that is just bigger than until"""
    i = 1
    while until > i*i:
        i += 2
    return i


if __name__ == "__main__":
    number = int(sys.argv[1])

    # the spiral is pattern that is made up
    # of an odd-numbered square
    # with a the sidelength being the root of the odd-square
    #   1) find the odd square number that is just bigger than the provided number
    #   2) get the sidelength figure out the directional position of the number
    #   3) get the correct position of the number on the side-chain
    #   4) calculate the manhattan distance

    odd = find_odd_square(number)
    dist = abs(odd**2-number)
    print("number: {}\tOdd-Square: {} = {}², distance from until: {}".format(number, odd*odd, odd, dist))

    direction = int(dist/(odd-1))
    # print("Distance: {}, on Side: {}".format(dist, direction))

    if direction%2 == 0:
        # upper and lower side-chain
        x_dist = abs(int(odd/2)-dist)
        y_dist = int(odd/2)
    else:
        # left and right side-chain
        tmp_dist = abs(((odd-1)*direction)-dist)
        y_dist = abs(int(odd/2)-tmp_dist)
        x_dist = int(odd/2)

    print("Steps to be taken in Manhattan distance: {}".format(x_dist+y_dist))


