from copy import deepcopy
import random
import time
from classes import Block, Grid

def main():
    active = Grid(rows=18, cols=10)
    static = Grid(rows=18, cols=10)
    blocks = []
    for _ in range(5):
        blocks.append(Block())
    for i in blocks:
        fall(active, static, i)


def copy(active, static):
    static = deepcopy(active)
    active = Grid(rows=18, cols=10)
    return active, static

def fall(active, static, block):
    posX = random.randint(0, static.cols - 10)
    for posY in range(static.rows - 4):
        time.sleep(0.5)
        active, static = copy(render_shape(active, block, posX, posY), static)
        print(static)

def render_shape(grid, block, posX, posY):   
    # Draw a block on grid. posX and posY refer to the position of the top left corner. 
    for y_index, y_value in enumerate(block.block):
        for x_index, x_value in enumerate(y_value):
            if x_value != 0:
                grid.grid[y_index + posY][x_index + posX] = 1
    return grid



def check_collision():
    ...

if __name__ == "__main__":
    main()

# I should try and make different blocks. They would need a class for representation, I believe.
# I guess I should make a different class for them. But how would I represent them? That's not exactly
# easy. I know I would be needing a 4x4 block for representing them, though..Maybe a list of lists?
# Can't see any other way...except Dicts.