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


def find_the_unbalanced_program(tree, root, curr_unbalanced="", curr_weight=0):
    """calc the sum of all candidates"""
    candidates = [ n for n,v in tree.items() if v["children"] ]

    # calculate the overall sum of each stack and save it
    for c in candidates:
        ws = [ tree[w]['size'] for w in tree[c]['children'] ]
        # print(c, ws, sum(ws)+tree[c]['size'])
        tree[c]['sumsize'] = tree[c]['size'] + sum(ws)

    # go depth first through the tree starting with the root
    bal = __traverse__(tree, root)
    print(bal, tree[bal])

    # find the parent of the balanced bal
    for c in candidates:
        if bal in tree[c]['children']:
            unbal = c
            break
    print(c, tree[c])



def __traverse__(tree, node):
    # check if sum of balanced stacks
    stack = [ tree[c]['sumsize'] for c in tree[node]['children'] ]

    if len(set(stack)) == 1:
        return node
    else:
        for ch in tree[node]['children']:
            return __traverse__(tree, ch)




def __find_unbalanced__(tree, node, unbal="", lst=[]):
    # base case
    child_sizes = [ tree[c]['sumsize'] for c in tree[node]['children'] ]
    if len(set(child_sizes)) <= 1:
        unbal, lst = node, child_sizes
    else:
        for c in tree[node]['children']:
            __find_unbalanced__(tree, c)
    return unbal, lst



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

    # find wrongly weighted program
    wrong = find_the_unbalanced_program(tree, first)
