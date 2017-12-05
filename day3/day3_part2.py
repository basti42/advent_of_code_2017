#!/usr/bin/env python3

import sys


def find_next_spiralnumber(number):
    grid = [[0] * 101 for _ in range(101)]
    step = 1
    grid[50][50] = 1
    x = 51
    y = 51
    num = number


    sumaround = lambda grid, x, y: grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1] + grid[x][y-1] + grid[x+1][y-1] + grid[x+1][y] + grid[x][y+1] + grid[x+1][y+1]

    while True:
        for i in range(2 * step - 1):
            y -= 1
            grid[x][y] = sumaround(grid, x, y)
            if grid[x][y] > num:
                return grid[x][y]
        for i in range(2 * step - 1):
            x -= 1
            grid[x][y] = sumaround(grid, x, y)
            if grid[x][y] > num:
                print(grid[x][y])
        for i in range(2 * step - 1):
            y += 1
            grid[x][y] = sumaround(grid, x, y)
            if grid[x][y] > num:
                return grid[x][y]
        for i in range(2 * step - 1):
            x += 1
            grid[x][y] = sumaround(grid, x, y)
            if grid[x][y] > num:
                return grid[x][y]
        step += 1
        x += 1
        y += 1


if __name__ == "__main__":
    number = int(sys.argv[1])

    next_num = find_next_spiralnumber(number)
    print("Number following {}: {}".format(number, next_num))
