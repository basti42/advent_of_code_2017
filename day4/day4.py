#!/usr/bin/env python3

"""
Advent of Code - Day 4
    Part 1 --> solved
    Part 2 -->
"""

def count_valid_passphrases(passphrases):
    """count and return the number of valid passphrases"""
    valid = 0
    for row in passphrases:
        if len(row) == len(set(row)):
            valid += 1
    return valid


def count_valid_no_anagrams(passphrases):
    """
    count and return the number of valid passphrases
    that are not the same words and not anagrams of each other
    """
    valid = 0
    for row in passphrases:
        # sort each word in the row alphabetically
        # then see of the set conversion is the same length as the row
        # if so: then no anagrams are present and the row is a valid passphrase
        r = [ "".join(sorted(word)) for word in row ]
        if len(r) == len(set(r)):
            valid += 1

    return valid



if __name__ == "__main__":

    with open("../testing_inputs/passphrases.txt", "r") as inp:
        f = inp.read()
        passphrases = [ row.split() for row in f.split("\n") if len(row)>0 ]

        valid = count_valid_passphrases(passphrases)
        print("Number of valid passphrases Policy_1: {}".format(valid))

        newvalid = count_valid_no_anagrams(passphrases)
        print("Number of valid passphrases Policy_2: {}".format(newvalid))
