from io import TextIOWrapper
import copy


def partOne(input: TextIOWrapper):
    grid = []
    total = 0
    accessible = []
    for line in input:
        grid.append([char=="@" for char in line.strip()])
    for i, row in enumerate(grid):
        for j, occupied in enumerate(row):
            surrounding = 0
            if occupied:
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[i]) and grid[x][y] and not (x == i and y == j):
                            surrounding += 1
                if (surrounding < 4):
                    total += 1
            grid[i][j] = surrounding
            
    # for row in grid:
    #     for roll in row:
    #         if roll == 0:
    #             print(roll, end="")
    #         elif roll < 4:
    #             print("\033[92m"+str(roll)+"\033[0m", end="")
    #         else:
    #             print("\033[91m"+str(roll)+"\033[0m", end="")
    #     print()
    return total                       
    pass

def partTwo(input):
    grid = []
    total = 0
    next = []
    for line in input:
        next.append([char=="@" for char in line.strip()])
    while grid != next:
        print(total)
        grid = copy.deepcopy(next)
        for i, row in enumerate(grid):
            for j, occupied in enumerate(row):
                surrounding = 0
                if occupied:
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):
                            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[i]) and grid[x][y] and not (x == i and y == j):
                                surrounding += 1
                    if (surrounding < 4):
                        total += 1
                        next[i][j] = False
    # for row in grid:
    #     for roll in row:
    #         if roll:
    #             print("@", end="")
    #         else:
    #             print(".", end="")
    #     print()
    return total