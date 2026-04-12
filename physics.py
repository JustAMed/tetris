import time
from termcolor import colored
from classes import Block, Grid
import random

def main():
    grid = Grid(rows=18, cols=10)
    block = Block()

    print(grid)
    fall(grid, block)

def fall(grid, block):
    y_offset = 0
    x_offset = random_col(grid)
    for i in range(5):
        # check_collision()
        render(grid, block, x_offset, y_offset)
        y_offset += 1
        print(grid)
    return grid

def random_col(grid):
    return random.randint(0, grid.cols - 4)

def render(grid, block, x_offset, y_offset):
    y_val = -1
    for y in enumerate(block.block):
        if y != [0,0,0,0]:
            continue;
        y += 1
        for x in y:
            grid.grid[y_val + y_offset][x + x_offset] = 1

    return grid

def check_collision(grid, pos, i):
    return i+1 == grid.rows or grid.grid[i+1][pos] == 1

if __name__ == "__main__":
    main()

# I should try and make different blocks. They would need a class for representation, I believe.
# I guess I should make a different class for them. But how would I represent them? That's not exactly
# easy. I know I would be needing a 4x4 block for representing them, though..Maybe a list of lists?
# Can't see any other way...except Dicts.