import time
from termcolor import colored
from blocks import Block

def main():
    rows = 18
    cols = 10
    grid = make_grid(rows, cols)
    
    print_grid(grid)
    test(grid, rows)

def make_grid(rows, cols):
    grid = []
    for _ in range(rows):
        tmp = []
        for _ in range(cols):
            tmp.append(0)
        grid.append(tmp)

    return grid

def test(grid, rows):
    for i in range(10):
        for _ in range(18):
            fall_test(grid, i, rows)

def print_grid(grid):
    for i in grid:
        row = []
        for j in i:
            if j == 1:
                row.append(colored(j, "red"))
            elif j == 0:
                row.append(colored(j, "green"))
        print(*row)
    print("\n")

def fall_test(grid, pos, rows):
    i = 0
    while True:
        grid[i][pos] = 1
        if i != 0:
            grid[i-1][pos] = 0
        time.sleep(0.01)
        print_grid(grid)
        if check_collision(grid, pos, rows, i) == True:
            break
        i += 1
    
    return grid

def check_collision(grid, pos, rows, i):
    return i+1 == rows or grid[i+1][pos] == 1

if __name__ == "__main__":
    main()

# I should try and make different blocks. They would need a class for representation, I believe.
# I guess I should make a different class for them. But how would I represent them? That's not exactly
# easy. I know I would be needing a 4x4 block for representing them, though..Maybe a list of lists?
# Can't see any other way.