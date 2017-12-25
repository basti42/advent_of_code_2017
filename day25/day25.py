#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 25
    The Halting Problem
"""


def checksum_after_time(todos, start, until):
    """
    return the sum of all ones after until runs,
    throught the registers, with the todos commands being
    executed
    """
    currReg = start
    tape = [0]
    idx = 0

    for i in range(until):

        # find the value of the current position on the tape
        # obtain the commands to be executed from
        # the todos dict based on the currCondition, seen

        currVal = tape[idx]
        cmds = todos[currReg][currVal]

        # write the value
        tape[idx] = int(cmds[0])

        # move the tape
        add = 1 if cmds[1] == 'right' else -1
        if idx+add >= len(tape)-1:
            tape.append(0)
            idx = idx + add
        elif idx+add <= 0:
            tape.insert(0,0)
            idx = idx
        else:
            idx = idx + add

        # continue with register
        currReg = cmds[2]

    return sum(tape)


if __name__ == "__main__":

    filename = "../testing_inputs/turing.in"
    states = {}
    with open(filename) as inp:
        lines = [ line.rstrip() for line in inp.readlines() ]

    # read the initial information from the first two lines of the input
    start = lines[0].split()[3][:-1]
    time2checksum = int(lines[1].split()[5])

    print("Start at state: {}".format(start))
    print("Times to checksum: {}".format(time2checksum))

    # drop the first 3 lines, cause we have that information 
    # and don't need the empty line
    lines = lines[3:]

    todos = {}
    currState, condition, cmd = "", "", ""
    for line in lines:
        if line.lstrip().startswith("In state"):
            currState = line.split()[2][:-1]
            todos[currState] = {}

        if line.lstrip().startswith("If"):
            condition = int(line.lstrip().split()[5][:-1])
            todos[currState][condition] = []

        if line.lstrip().startswith("-"):
            cmd = line.lstrip()[2:-1]
            cmd = cmd.split()[-1]
            todos[currState][condition].append(cmd)

    # PART 1
    checksum = checksum_after_time(todos.copy(), start, time2checksum)
    print("Checksum after some runs: {}".format(checksum))
