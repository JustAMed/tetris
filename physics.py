import time
from copy import deepcopy
from termcolor import colored
from classes import Block, Grid
import random

def main():
    grid = Grid(rows=18, cols=10)
    block = Block()
    fall(grid, block)

def pyg_render():
    pass

def fall(grid, block):
    block.x_offset = random_col(grid)
    while True:
        block.y_offset += 1
        if check_collision(grid, block):
            draw_block(grid, block)
            break
        pyg_render()
        return grid

def draw_block(grid, block):
    for y_val, y in enumerate(block.block):
        for x_val, x in enumerate(y):
            if x == 1:
                grid[y_val + block.y_offset][x_val + block.x_offset] = 1

    return grid

def random_col(grid):
    return random.randint(0, grid.cols - 4)

def check_collision(grid, block):
    for y_val, y in enumerate(block.block):
        for x_val, x in enumerate(y):
            if x == 1:
                if (grid.grid[y_val + block.y_offset + 1][x_val + block.x_offset]) == 1:
                    return True

    

if __name__ == "__main__":
    main()

