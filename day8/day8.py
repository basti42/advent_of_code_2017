#!/usr/bin/env python3


def make_move(register, name, anw, step, cond, currMax):
    """cond is in for elem comparator number"""
    elem, comp, vgl = cond.split(" ")

    # check if elem exists if not it is 0
    currval = 0 if elem not in register else register[elem]

    if eval(str(currval)+comp+vgl):
        update = 1 if anw == 'inc' else -1
        step = int(step)

        if name not in register:
            register[name] = 0 + update*step
            if register[name] > currMax: currMax = register[name]
        else:
            register[name] += update*step
            if register[name] > currMax: currMax = register[name]

    return register, currMax



if __name__ == "__main__":

    filename = "../testing_inputs/reg.txt"
    with open(filename) as inp:
        lines = inp.read().split("\n")

    register = dict()
    currMax = 0

    for line in lines:
        if not line: continue

        # split the line and save into variables
        part = lambda l : (l.split(" ")[0], l.split(" ")[1], l.split(" ")[2], " ".join(l.split(" ")[3:])[3:])
        name, anw, step, cond = part(line)

        # make a move if the cond validates to True
        # and create the register elements on the fly
        register, currMax = make_move(register, name, anw, step, cond, currMax)


    # print(register)
    maxval = max(list(register.values()))
    print("Max value in the register after list: {}".format(maxval))
    print("Max value ever held in any register: {}".format(currMax))




