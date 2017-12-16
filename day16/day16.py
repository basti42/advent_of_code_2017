#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 16
    Permutation Promenade
"""


def make_moves(liste, moves):
    """
    perform the changes on the list according to the moves
    """
    for move in moves:

        # spin X elements from the end to the front of the list
        if move.startswith("s"):
            idx = int(move[1:])
            liste = liste[-idx:] + liste[:-idx]

        # exchange programs at postions x,y
        elif move.startswith('x'):
            x,y = [ int(i) for i in move[1:].split("/") ]
            tmp = liste[x]
            liste[x] = liste[y]
            liste[y] = tmp

        # switch program a with program b
        elif move.startswith("p"):
            ia, ib = [ liste.index(j) for j in move[1:].split("/") ]
            tmp = liste[ia]
            liste[ia] = liste[ib]
            liste[ib] = tmp
    return liste


def billion_dances(liste, moves):
    """
    10**9-1 time perform the dance, cause liste is already the
    sequence after the first dance
    dynamic programming would make sense here
    """
    observed = []
    result = liste

    for i in range(10**9):

        curr = "".join(result)

        if curr in observed:
            # print("Cycle: {}".format(i))
            return observed[10**9 % i]

        observed.append(curr)
        result = make_moves(result, moves)


if __name__ == "__main__":

    inp = [ c for c in 'abcdefghijklmnop' ]
    filename = "../testing_inputs/moves.txt"
    with open(filename) as f_in:
        moves = f_in.read().strip().split(",")

    result = make_moves(inp[:], moves)
    print("Sequence of program after one dance: {}".format("".join(result)))

    res = billion_dances(inp[:], moves)
    print("Sequence of programs after 10^9 dances: {}".format("".join(res)))
