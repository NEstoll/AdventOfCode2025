from io import TextIOWrapper

def partOne(input: TextIOWrapper):
    shapes = {}
    regions = []
    last = -1
    for line in input:
        if line.strip() == "":
            last = -1
            continue
        if line.strip().endswith(":"):
            last = int(line.rstrip(":\n"))
            shapes[last] = []
            continue
        if last != -1:
            shapes[last].append([c=="#" for c in line])
        else:
            regions.append((tuple([int(s) for s in line.split(":")[0].split("x")]), [int(c) for c in line.split(":")[1].strip().split(" ")]))
    working = 0
    for area, presents in regions:
        if (area[0]//3)*(area[1]//3) >= sum(presents): #always works
            # print(area, "always works")
            working += 1
            continue
        if sum([sum([sum(b) for b in shapes[i]])*count for i, count in enumerate(presents)]):
            # print(area, "always fails")
            continue
        grid = [[False for x in range(area[0])] for y in range(area[1])]
        #all shapes are 3x3
    return working
            
def place(grid, shape, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if grid[x+i][y+j] and shape[i][j]:
                raise Exception("can't overlap")
            else:
                grid[x+i][y+j] = grid[x+i][y+j] or shape[i][j]

def partTwo(input: TextIOWrapper):
    pass