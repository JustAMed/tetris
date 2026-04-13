import time
from termcolor import colored
from classes import Block, Grid
import random

def main():
    grid = Grid(rows=18, cols=10)
    block = Block()
    grid = fall(grid, block)

def fall(grid, block):
    block.x_offset = random_col(grid)
    while True:
        delete(grid, block)
        block.y_offset += 1
        if check_collision(grid, block) == True:
            render(grid, block)
            print(grid)
            return grid
        hello = render(grid, block)
        if not hello:
            break
        print(grid)
        time.sleep(0.2)

    return grid

def random_col(grid):
    return random.randint(0, grid.cols - 4)

def delete(grid, block):
    # for x,y in block, erase i-1 unless it's 0
    for y_pos, y in enumerate(block.block):
        for x_pos, x in enumerate(y):
            if x == 1:
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
    # check ground collison by checking if y offset + num of rows in block == grid.rows
    for y_val, y in enumerate(block.block):
        for x_val, x in enumerate(y):
                if x == 1:
                    if y_val + block.y_offset + 1 >= grid.rows:
                        return True
                    if grid.grid[y_val + block.y_offset + 1][x_val + block.x_offset] == 1:
                        return True
    return False 


if __name__ == "__main__":
    main()

