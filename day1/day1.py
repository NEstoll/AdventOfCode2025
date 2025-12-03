def partOne(file):
    dial = 50
    password = 0
    input = file
    for line in input:
        if line[0] == 'R':
            for i in range(int(line.strip("R"))):
                dial = (dial + 1)%100
            if (dial == 0):
                password += 1
        else:
            for i in range(int(line.strip("L"))):
                dial = (dial - 1)%-100
            if (dial == 0):
                password += 1
    return password

def partTwo(file):
    dial = 50
    password = 0
    input = file
    for line in input:
        if line[0] == 'R':
            for i in range(int(line.strip("R"))):
                dial = (dial + 1)%100
                if (dial == 0):
                    password += 1
        else:
            for i in range(int(line.strip("L"))):
                dial = (dial - 1)%-100
                if (dial == 0):
                    password += 1
    return password