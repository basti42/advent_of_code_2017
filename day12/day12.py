#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 12
    Digital Plumber
"""

def find_group(progs):
    """
    Breadth first search to find progs connected to 0
    Starting with children for prog 0
        every children of prog 0 and subsequent their children
        are connected to prog 0 (queue)
    checking if against a set of already visited progs
    """
    queue = [0]
    visited = set()

    while queue:
        # until there are candidates in queue, check their children if they are already seen

        curr = queue.pop()

        for child in progs[curr]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return visited


def count_groups(progs):
    """using the same algoithm as above, but only caring about the nums of new groups"""
    visited = set()
    count = 0

    for i in range(len(progs)):

        # if prog i already in visited, skip
        if i in visited: continue

        count += 1

        # check the group for prog i
        queue = [i]
        while queue:
            curr = queue.pop()
            for child in progs[curr]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
    return count


if __name__ == "__main__":

    progs = {}
    filename = "../testing_inputs/pipes.txt"
    with open(filename) as inp:
        for line in inp:
            curr, _, children = line.split(maxsplit=2)
            progs[int(curr)] = list(map(int, children.split(", ")))

    group = find_group(progs)
    print("Elements in group 0: {}".format(len(group)))

    group_count = count_groups(progs)
    print("Number of overall groups: {}".format(group_count))
