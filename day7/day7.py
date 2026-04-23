from io import TextIOWrapper

def partOne(input: TextIOWrapper):
    last = set()
    splits = 0
    for line in input:
        next = set()
        if len(last) == 0:
            next.add(line.index("S"))
        else:
            for beam in last:
                if line[beam] == "^":
                    next.add(beam-1)
                    next.add(beam+1)
                    splits += 1
                else:
                    next.add(beam)
        last = next
    return splits
    pass

def partTwo(input):
    last = {}
    splits = 1
    for line in input:
        next = {}
        if len(last) == 0:
            next[line.index("S")] = 1
        else:
            for index, count in last.items():
                if line[index] == "^":
                    next[index-1] = count + next.get(index-1, 0)
                    next[index+1] = count + next.get(index+1, 0)
                    splits += count
                else:
                    next[index] = count+ next.get(index, 0)
        last = next
        # print(splits, sum(last.values()))
    return sum(last.values())
    pass