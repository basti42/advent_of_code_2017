#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 22
    Sporifica Virus
"""

def count_infections(grid, pos, until=10000):
    """count the number of new infections"""

    direction = 'N'
    infections = 0

    turnleft = { 'N':[(0,-1), 'W'], 'E':[(-1,0), 'N'], 'S':[(0,1), 'E'], 'W':[(1,0), 'S'] }
    turnright = { 'N':[(0,1), 'E'], 'E':[(1,0), 'S'], 'S':[(0,-1), 'W'], 'W':[(-1,0), 'N'] }

    for i in range(until):

        if not grid[pos]: infections += 1

        # check if the current field is infected
        if grid[pos]:
            newpos, direction = turnright[direction]
        else:
            newpos, direction = turnleft[direction]

        addrow, addcol = newpos
        prevpos = (pos[0], pos[1])
        pos = (pos[0]+addrow, pos[1]+addcol)

        # check if pos is in grid
        if pos not in grid:
            grid[pos] = False

        # update prev position
        if grid[prevpos]: grid[prevpos] = False
        else: grid[prevpos] = True

    return infections


def count_evolved_virus_infections(grid, pos, until=10000000):
    """count the number of new infections"""

    direction = 'N'
    infections = 0

    turnleft = { 'N':[(0,-1), 'W'], 'E':[(-1,0), 'N'], 'S':[(0,1), 'E'], 'W':[(1,0), 'S'] }
    turnright = { 'N':[(0,1), 'E'], 'E':[(1,0), 'S'], 'S':[(0,-1), 'W'], 'W':[(-1,0), 'N'] }
    rev = { 'N':[(1,0), 'S'], 'E':[(0,-1), 'W'], 'S':[(-1,0), 'N'], 'W':[(0,1), 'E'] }
    cont = { 'N':[(-1,0), 'N'], 'E':[(0,1), 'E'], 'S':[(1,0), 'S'], 'W':[(0,-1), 'W'] }

    for i in range(until):

        if grid[pos] == 'W': infections += 1

        # update the position and directions
        if grid[pos] == 'F':                                # flagged - reverse direction
            newpos, direction = rev[direction]
        elif grid[pos] == 'W':                              # weakened - continue direction
            newpos, direction = cont[direction]
        elif not grid[pos]:                                 # clean - turn left
            newpos, direction = turnleft[direction]
        elif grid[pos]:                                     # infected - turn right
            newpos, direction = turnright[direction]

        addrow, addcol = newpos
        prevpos = (pos[0], pos[1])
        pos = (pos[0]+addrow, pos[1]+addcol)

        # check if pos is in grid
        if pos not in grid:
            grid[pos] = False

        # update prev position
        if not grid[prevpos]:grid[prevpos] = 'W'            # clean
        elif grid[prevpos] == 'W': grid[prevpos] = True     # weakend
        elif grid[prevpos] == 'F': grid[prevpos] = False    # flagged
        elif grid[prevpos]: grid[prevpos] = 'F'             # infected

    return infections


if __name__ == "__main__":

    filename = "../testing_inputs/infected_grid.txt"
    with open(filename) as inp:
        lines = [ line.strip() for line in inp.readlines()]

    # using a dict with tuple coordinates to simulate a grid
    # adding items to the grid if the coordinte tuple is not yet included
    grid = {}
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            grid[(row,col)] = c=='#'

    start = (12,12)     # starting position, no need to make fancy coordinate mapping

    new_infects = count_infections(grid.copy(), start)
    print("Normal virus infections: {}".format(new_infects))

    evolved = count_evolved_virus_infections(grid.copy(), start)
    print("Evolved virus infections: {}".format(evolved))
