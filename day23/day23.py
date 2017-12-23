#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 23
    Coprocessor Conflagration
"""

def count_multiplications(instructions, register, partb=False):
    """
    count how many times the mul command is being invoked
    """
    mul_num, pointer = 0, 0
    if partb: register['a'] = 1

    while pointer<len(instructions):

        cmd, a, b = instructions[pointer]

        if cmd == 'set':
            val = register[b] if b in 'abcdefgh' else int(b)
            register[a] = val
            pointer += 1

        elif cmd == 'sub':
            val = register[b] if b in 'abcdefgh' else int(b)
            register[a] -= val
            pointer += 1

        elif cmd == 'mul':
            mul_num += 1
            val = register[b] if b in 'abcdefgh' else int(b)
            register[a] *= val
            pointer += 1

        elif cmd == 'jnz':
            val = register[a] if a in 'abcdefgh' else int(a)
            if val != 0:
                pointer += int(b)
            else:
                pointer += 1

    if not partb:
        return mul_num
    else:
        return register['h']


if __name__ == "__main__":

    filename = "../testing_inputs/day23.in"
    with open(filename) as inp:
        lines = [ line.strip().split() for line in inp.readlines() ]

    # initialize the registers a..h with value 0
    registers = { chr(i):0 for i in range(97,105) }

    multimes = count_multiplications(lines[:], registers.copy())
    print("Number of times multiply was invoked: {}".format(multimes))

