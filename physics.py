import time
import os
from termcolor import colored
from classes import Block, Grid
import random

def main():
    grid = Grid(rows=18, cols=10)
    block = Block()
    render_shape(block)

def fall(grid, block):
    i = 0
    for y in block.block:
        for x in y:
            if x == 1:
                print("@")
    return grid

def render_shape(block):
    res = ""
    for y in block.block:
        for x in y:
            if x == 1:
                res += "#"
            elif x == 0:
                res += " "
        res += "\n"
    print(res.rstrip())

def check_collision(grid, pos, i):
    return i+1 == grid.rows or grid.grid[i+1][pos] == 1

if __name__ == "__main__":
    main()

# I should try and make different blocks. They would need a class for representation, I believe.
# I guess I should make a different class for them. But how would I represent them? That's not exactly
# easy. I know I would be needing a 4x4 block for representing them, though..Maybe a list of lists?
# Can't see any other way...except Dicts.