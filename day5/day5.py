#!/usr/bin/env python3

"""
Advent of Code 2017 - Day 5
    PART 1: Escaping a List of numbers
    PART 2: differing the offsets de/increase based on seen value
"""

def hop_through_list(lst, part=1):
    """actual list jumping with incrementing visited indices"""
    steps, idx = 0, 0

    while 0<=idx<len(lst):

        # obtain current value, increment current list offset, update idx with value, and increment steps
        val = lst[idx]

        if part == 1:
            lst[idx] += 1
        else:
            if val > 2: lst[idx] -= 1
            else: lst[idx] += 1

        idx += val
        steps += 1

        # print("step {}: {}".format(steps, lst))
    return steps


if __name__ == "__main__":

    filename = "../testing_inputs/list.txt"
    with open(filename, "r") as inp:
        lst = inp.read()
    # need 2 lists, since i modify the elements in lst
    lst = [int(n) for n in lst.split("\n") if len(n)>0 ]
    lst2 = [n for n in lst]

    steps = hop_through_list(lst)
    print("Part1: Leaving the list after {} steps!".format(steps))

    part2 = hop_through_list(lst2, part=2)
    print("Part2: Leaving the list after {} steps!".format(part2))
