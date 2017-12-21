#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 21
    Fractal Art
"""

import numpy as np

def count_on(field, repl, times=5):
    """actual fractal growing"""
    size = len(field)
    pattern = field.copy()

    for t in range(times):

        if size % 2 == 0:
            newsize = size // 2 * 3
            npattern = np.empty((newsize, newsize), dtype=bool)
            for i in range(0, size, 2):
                for j in range(0, size, 2):
                    npattern[i//2*3:i//2*3+3,j//2*3:j//2*3+3] = repl[pattern[i:i+2, j:j+2].tobytes()]
        # size % 3 == 0
        else:
            newsize = size // 3 * 4
            npattern = np.empty((newsize, newsize), dtype=bool)
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    npattern[i//3*4:i//3*4+4,j//3*4:j//3*4+4] = repl[pattern[i:i+3, j:j+3].tobytes()]
        pattern = npattern
        size = newsize
    # numpy comes with an easy counter for all True values
    return sum(sum(pattern))



if __name__ == "__main__":

    filename = "../testing_inputs/fractal_rules.txt"
    with open(filename) as inp:
        lines = inp.readlines()

    replace = {}
    for line in lines:
        inpu, outp = line.split(" => ")

        # make bool np arrays from the input, easier Count for on values
        inpu = np.array([[ c == '#' for c in comp] for comp in inpu.split("/") ])
        outp = np.array([[ c == '#' for c in comp] for comp in outp.split("/") ])
        flipped_inpu = np.flipud(inpu)

        # create dict for replacing the patterns
        # key is a byte-converted np.array
        for i in range(4):
            replace[inpu.tobytes()] = outp
            replace[flipped_inpu.tobytes()] = outp
            inpu, flipped_inpu = np.rot90(inpu), np.rot90(flipped_inpu)

    # Beginning pattern
    start = np.array([[False, True, False],[False, False, True],[True, True, True]])

    part1 = count_on(start.copy(), replace, times=5)
    print("Part 1: After 5 Iterations ON: {}".format(part1))

    part2 = count_on(start.copy(), replace, times=18)
    print("Part 2: After 18 Iterations ON: {}".format(part2))

