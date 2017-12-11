#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 11
    Hexgrid distance calculation
"""

def calc_move_nums(moves):
    """using x,y,z coordinates for hex grids"""
    # initializing vars for coordinates and holding the max distance
    x,y,z = 0,0,0
    furthest = 0

    for move in moves:
        #
        # update coordinate variables accordingly
        #
        if move == "n":
            y += 1
            z -= 1
        elif move == "s":
            y -= 1
            z += 1
        elif move == "ne":
            x += 1
            z -= 1
        elif move == "se":
            x += 1
            y -= 1
        elif move == "nw":
            x -= 1
            y += 1
        elif move == "sw":
            x -= 1
            z += 1

        # Formular for calculating the distance in hexgrids
        # https://www.redblobgames.com/grids/hexagons/#distances

        curr_dist = (abs(x) + abs(y) + abs(z))/2
        # if current distance if more than the current furthest: set it
        if curr_dist > furthest: furthest = curr_dist

    return curr_dist, furthest


if __name__ == "__main__":

    filename = "../testing_inputs/hex.txt"
    with open(filename) as inp:
        moves = inp.read().strip().split(",")

    num_moves, furthest = calc_move_nums(moves)
    print("Steps to reach the final field: {}".format(int(num_moves)))
    print("The furthest distance ever was: {}".format(int(furthest)))
