from termcolor import colored

class Block:
    def __init__(self):
        blocks = {
            'I': [
                0, 0, 0, 0,
                1, 1, 1, 1,
                0, 0, 0, 0,
                0, 0, 0, 0
            ]
        }
        self.block = blocks['I']

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
        return f"{'\n'.join(lines)}\n\n\n\n"
    
    