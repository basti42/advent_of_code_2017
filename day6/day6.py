#!/usr/bin/env python3

"""
Advent of Code - Day 6
    Part 1/2 --> SOLVED
    Redistributing blocks in a given set of memory banks
"""

def count_until_recurring(blocks):

    # keep track of the states and cycles
    # states as a dict, with current state as key and overall cycle number as value
    # so the infinite loop cycle is the exitingIndex - states[currBlockConfiguration]
    states, cycles = dict(), 0

    counter = 0
    while tuple(blocks) not in states:

        states[tuple(blocks)] = counter   #current state to be kept track of
        counter += 1

        # 1) find highest number bank
        # 2) redistribute blocks
        # 3) update cycles

        # the first occurence of the max value in the list is the bank to use
        # since .index(max(blocks)) returns the first occurence of the max value
        # no further checking against other occurences of max(blocks) in the blocks is needed

        maxidx = blocks.index(max(blocks))
        num_blocks = blocks[maxidx]
        blocks[maxidx] = 0

        # redistribute
        i = maxidx + 1
        while num_blocks > 0:
            blocks[i%len(blocks)] += 1
            num_blocks -= 1
            i += 1

        # update cycles
        cycles += 1

    inf_loop_cycles = counter - states[tuple(blocks)]
    return cycles, inf_loop_cycles


if __name__ == "__main__":

    filename = "../testing_inputs/blocks.txt"
    with open(filename, "r" ) as inp:
        blocks = inp.readline().rstrip()

    blocks = [ int(b) for b in blocks.split(" ") if len(b)>0 ]

    # Part 1 and Part 2 solved in 1 method
    # using a dict instead of just a set

    cycles, inf_loop_cycles = count_until_recurring(blocks)
    print("Recurrence reached after {} cycles.".format(cycles))
    print("Infinite loop cycles: {}".format(inf_loop_cycles))
