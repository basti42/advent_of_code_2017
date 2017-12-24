#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 24
    Electromagnetic Moat
    recursively building bridges
"""

all_bridges = []

def find_max():
    """weird helper function for filtering all NoneTypes, whereeer they came from"""
    bridges = all_bridges
    bridges = [ b for b in bridges if b != None ]
    return max(bridges)

def build_bridge(blocks):
    """starting from the starting blocks"""
    bridges = []
    for start in [ b for b in blocks if 0 in b ]:
        tmp = blocks[:]
        tmp.remove(start)
        bridges.append(build(tmp, start[1], [start], sum(start)))
    return find_max()

def build(pieces, connector, bridge, currLen):
    """recursive build, append each new bridge to all_bridges"""
    children = [ b for b in pieces if connector in b]
    if children == None or len(children) <= 0:
        return currLen, bridge

    else:
        for child in children:
            conn = child[0] if child[1]==connector else child[1]
            available = pieces[:]
            available.remove(child)
            all_bridges.append(build(available, conn, bridge +[child], currLen+sum(child)))

def strength_longest_bridge():
    """find the strength of the longest bridge"""
    # first again filter all the Nonetype out
    bridges = [ b for b in all_bridges if b != None ]

    # the find the strength of the longest bridge
    # in this case the first longest to be found is also the
    # the strongest out of all the longest

    return max(bridges, key=lambda b: len(b[1]))[0]


if __name__ == "__main__":

    filename = "../testing_inputs/domino.in"
    with open(filename) as inp:
        lines = [ tuple(map(int, line.strip().split("/"))) for line in inp.readlines() ]

    bridge = build_bridge(lines[:])
    print("Strength of the strongest bridge: {}".format(bridge[0]))

    longest = strength_longest_bridge()
    print("Strength of the longst bridge: {}".format(longest))
