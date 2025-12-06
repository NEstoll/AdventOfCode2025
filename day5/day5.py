def partOne(input):
    ranges = True
    fresh = []
    availible = []
    total = 0
    for line in input:
        if line == "\n":
            ranges = False
            continue
        if ranges:
            start, end = line.split("-")
            fresh.append((int(start), int(end)))
        else:
            availible.append(int(line))
    for id in availible:
        good = False
        for start, end in fresh:
            if id >= start and id <= end:
                good = True 
                # print(id, "is between", start, "and", end)
        if good:
            total += 1
    return total



def partTwo(input):
    ranges = True
    fresh = []
    availible = {0}
    total = 0
    for line in input:
        if line == "\n":
            ranges = False
            continue
        if ranges:
            start, end = line.split("-")
            fresh.append((int(start), int(end)))
    toRemove = [0]
    while len(toRemove) != 0:
        toRemove.clear()
        for i, range in enumerate(fresh):
            for j, range2 in enumerate(fresh):
                if j <= i:
                    continue
                if range[0] <= range2[1] and range2[0] <= range[1]:
                    fresh[i] = (min(range[0], range2[0]), max(range[1], range2[1]))
                    range = (min(range[0], range2[0]), max(range[1], range2[1]))
                    toRemove.append(j)
                    # print(range, "and", range2, "overlap, reconfiguring to", fresh[i])
                    continue
            if len(toRemove) != 0:
                break
        fresh = [x for i, x in enumerate(fresh) if not i in toRemove]
    for start, end in fresh:
        total += end-start+1
    # print(fresh)
    return total