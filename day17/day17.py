#!/usr/bin/env python3


"""
Advent of Code 2017 - DAY 17
    Spinlock
"""

def find_value_after(liste, steps, until=2017):
    """
    1) from the initial state [0], step steps times throught the list
    2) insert new val after the stopping position on the list
    3) set this position to the new current pos and increment the val
    """

    currPos = 0
    for i in range(until):

        currPos = ((currPos+steps)%len(liste))+1
        liste.insert(currPos, i+1)

    return liste


def part2(liste, steps):
    """rewrite of mathod for part 2"""
    cur = 0
    before_len = 0
    after_len = 0
    after_num = 0

    for i in range(1, 50000001):
        cur = ((cur + steps) % (before_len + 1 + after_len)) + 1

        if cur == (before_len + 1):
            after_num = i
            after_len += 1
        elif cur > (before_len + 1):
            after_len += 1
        elif cur < (before_len + 1):
            before_len += 1
    return after_num



if __name__ == "__main__":

    steps = 301     # puzzle input
    liste = [0]     # initial list

    post2017 = find_value_after(liste[:], steps)
    print("Value after '2017': {}".format(post2017[post2017.index(2017)+1]))

    post0 = part2(liste[:], steps)
    print("Value after '0': {}".format(post0))
