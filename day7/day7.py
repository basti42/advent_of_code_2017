#!/usr/bin/env python3

import re

def find_name_of_first(tree):
    """Find the name of the first program, aka. the root of the tree """

    # candidates for the root, can only be the programs that have children
    # then check the names of theses for occurence in children-lists of the others
    # the root (first program) is the program that has children and is not a children
    # of any other program

    candidates = [ n for n,v in tree.items() if v["children"] ]

    # find the one candidate, that is not a child of another candidate
    for poss_first in candidates:

        isFirst = True

        # check if children in other (for now including self)
        for other in candidates:

            # no self checking
            if poss_first == other: continue
            # else
            if poss_first in tree[other]["children"]:
                isFirst = False
                break

        if isFirst:
            return poss_first
    # below here should never be reached


if __name__ == "__main__":

    filename = "../testing_inputs/tree.txt"
    with open(filename, "r") as inp:
        raw = inp.read()

    # tree = {name: { size: int, children: list }
    tree = dict()

    r_weight = re.compile("\d+")
    raw = raw.split("\n")

    for r in raw:
        # if r (=line in file) is empty, skip the line
        if len(r) < 1: continue

        # init the values for the tree-dict construction
        name = r[:r.index(" ")]
        size = int(re.search(r_weight, r).group())

        # check if the program balances other programs
        if ">" in r:
            raw_children = r[r.find(">")+1:]
            children = raw_children.split(",")
            children = [ n.rstrip().lstrip() for n in children ]
        else:
            children = []

        # create the Node in the tree, if not children --> Leaf node
        tree[name] = { 'size': size, 'children': children }

#    # Testing
#    for k,v in tree.items():
#        print(k ,v)

    # find the name of the first program
    first = find_name_of_first(tree)
    print("The name of the first program is: {}".format(first))

