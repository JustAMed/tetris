import time
from termcolor import colored
from classes import Block, Grid
import random

def main():
    grid = Grid(rows=18, cols=10)
    block = Block()
    fall(grid, block)

def fall(grid, block):
    block.x_offset = random_col(grid)
    for i in range(18):
        # check_collision()
        render(grid, block)
        print(grid)
        delete(grid, block)
        block.y_offset += 1
        time.sleep(0.1)

    return grid

def random_col(grid):
    return random.randint(0, grid.cols - 4)

def delete(grid, block):
    # for x,y in block, erase i-1 unless it's 0
    for y_pos, y in enumerate(block.block):
        for x_pos, x in enumerate(y):
            grid.grid[y_pos + block.y_offset][x_pos + block.x_offset] = 0

    return grid


def render(grid, block):
    # cleanse
    for y_val, y in enumerate(block.block):
        for x_val, x in enumerate(y):
            if x == 1:
                grid.grid[y_val + block.y_offset][x_val + block.x_offset] = 1

    return grid


def check_collision(grid, block):
    # for x, y in block, if x, y+1 is 1, return True, else return False
    for y_val, y in enumerate(block.block):
        for x_val, x in enumerate(y):
            if x == 1:
                grid.grid[y_val + block.y_offset][x_val + block.x_offset] = 1
    return False 

if __name__ == "__main__":
    main()

# I should try and make different blocks. They would need a class for representation, I believe.
# I guess I should make a different class for them. But how would I represent them? That's not exactly
# easy. I know I would be needing a 4x4 block for representing them, though..Maybe a list of lists?
# Can't see any other way...except Dicts.