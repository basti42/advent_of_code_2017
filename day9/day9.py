#!/usr/bin/env python3

"""
Advent of Code - DAY 9
    Stream Processing - solved
"""

def count_groups(stream):
    """count the groups in the input stream"""
    # variables
    curr_num = 0
    group_sums = 0
    i = 0
    garbage = 0

    while i < len(stream):

        # skip the next char if a "!" is observed
        if stream[i] == "!":
            i += 1

        # incr curr_num if group opens
        elif stream[i] == "{": curr_num += 1

        # if group closes: add to group_sums and decr curr_num
        elif stream[i] == "}":
            group_sums += curr_num
            curr_num -= 1

        # skip all garbage characters until garbage is closed
        elif stream[i] == "<":

            # use subindex subi for looping over garbage
            subi = i+1

            while subi < len(stream):
                if stream[subi] == "!":
                    subi += 1
                elif stream[subi] == ">":

                    # count all valid values within the garbage
                    garbage += count_garbage(stream[i+1:subi])

                    i = subi
                    break

                # incr subcounter
                subi += 1

        # incr counter i
        i += 1
    return group_sums, garbage


def count_garbage(garb_stream):
    """count all valid characters in stream[start...stop] (incl. stop)"""
    garb, i = 0, 0
    while i < len(garb_stream):

        # skip and do not count character if "!" is observed
        if garb_stream[i] == "!":
            i += 1
        else:
            garb += 1
        i += 1
    return garb



if __name__ == "__main__":

    filename = "../testing_inputs/stream.txt"
    with open(filename) as inp:
        stream = inp.read()

    sum_of_groups, garbage = count_groups(stream.strip())
    print("Sum of all groups: {}".format(sum_of_groups))
    print("Sum of Garbage Elements: {}".format(garbage))



