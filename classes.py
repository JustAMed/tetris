from termcolor import colored
from random import choice
class Block:
    def __init__(self):
        blocks = {
            'I': [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            'J': [
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            'L': [
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            'O': [
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0]
            ],
            'S': [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0]
            ],
            'T': [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            'Z': [
                [1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
        }
        keys = list(blocks.keys())
        self.key = choice(keys)
        self._block = blocks[self.key]
        self.y_offset = 0
        self.x_offset = None

    @property
    def block(self):
        return self.cleanse(self._block)

    def cleanse(self, data):
        res = []
        for i in data:
            if i != [0,0,0,0]:
                res.append(i)
        return res
class Grid:
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.grid = []
        for _ in range(rows):
            tmp = []
            for _ in range(cols):
                tmp.append(0)
            self.grid.append(tmp)

    def __str__(self):
        lines = []
        for i in self.grid:
            row = []
            for j in i:
                if j == 1:
                    row.append(colored(j, "red"))
                elif j == 0:
                    row.append(colored(j, "green"))
            row = [str(v) for v in row]
            lines.append(" ".join(row))
        return f"{'\n'.join(lines)}\n"
    
    