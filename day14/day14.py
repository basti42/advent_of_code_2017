#!/usr/bin/env python3

import knothash as knot
# Code from Day 10, renamed, for better readability

"""
Advent of Code 2017 - DAY 14
    Disk Fragmentation
    Reusing Code from Day 10
"""

def count_used_squares(hashlist):
    """counting the number of used squares, denoted by 1 in bin hash"""
    used = 0
    for binhash in hashlist:
        used += binhash.count("1")
    return used


def count_regions(all_used):
    """
    counting number of connected squares (not diagonally connected) = regions
    Keeping track of all seen used squares, in 'all_used'
    Element by element in that list, find its children, and remove it from 'all_used'
    until no more children can be found, then increase the count of regions
    List of 'all_used' is decremented by every child connected to an already picked element from it
    """
    regions = 0
    while all_used:
        queue = [all_used[0]]
        while queue:
            (row, col) = queue.pop()
            if (row, col) in all_used:
                all_used.remove((row, col))
                # add all children of this node to the queue
                queue += [(row-1,col),(row, col+1), (row+1,col),(row,col-1)]

        regions += 1
    return regions


if __name__ == "__main__":

    # Set some Variables
    test = "flqrgnkx"
    raw = "nbysizxe"
    bin_hashes, all_used = [], []

    # create the bin hash for each row and save them
    for i in range(0,128):

        # make the knot_hash (knot.all_round_hash) for each row
        # then convert every hex digit to its 4digit binary representation

        row_bin_hash = ""

        # bin conversion, .zfill fills a string with 0 to the left, when hex digit <8
        for c in knot.all_round_hash(raw+"-"+str(i)):
            row_bin_hash += bin(int(c, 16))[2:].zfill(4)

        all_used += [ (i, col) for col, digit in enumerate(row_bin_hash) if digit == '1' ]
        bin_hashes.append(row_bin_hash)

    # Part 1: Number of used squares
    used_squares = count_used_squares(bin_hashes)
    print("Number of Used squares: {}".format(used_squares))

    # Part 2: Number of regions
    regions = count_regions(all_used)
    print("Number of connected regions of used squares: {}".format(regions))
