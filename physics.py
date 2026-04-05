import time
import os
from termcolor import colored
from classes import Block, Grid
import random

def main():
    grid = Grid(rows=18, cols=10)
    block = Block()

    print(grid)
    for _ in range(180):
        fall_test(grid, block)


def fall_test(grid, block):
    i = 0
    pos = random_col(grid)
    while True:
        grid.grid[i][pos] = 1
        if i != 0:
            grid.grid[i-1][pos] = 0
        time.sleep(0.01)
        print(grid)
        if check_collision(grid, pos, i) == True:
            break
        i += 1
    
    return grid

def random_col(grid):
    res = []
    for i in range(grid.cols):
        if grid.grid[0][i] == 0:
            res.append(i)
    return random.choice(res)

def check_collision(grid, pos, i):
    return i+1 == grid.rows or grid.grid[i+1][pos] == 1

if __name__ == "__main__":
    main()

# I should try and make different blocks. They would need a class for representation, I believe.
# I guess I should make a different class for them. But how would I represent them? That's not exactly
# easy. I know I would be needing a 4x4 block for representing them, though..Maybe a list of lists?
# Can't see any other way...except Dicts.