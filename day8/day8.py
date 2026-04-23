from io import TextIOWrapper

def partOne(input: TextIOWrapper):
    points = []
    connections = []
    possible = []
    for num, line in enumerate(input):
        points.append(tuple([int(s) for s in line.split(",")]))
    circuits = [{y} for y in points]
    for x, point in enumerate(points):
        for y, other in enumerate(points):
            if point is not other and y > x:
                possible.append((distance(point, other), {point, other}))
    possible.sort(key =lambda t: t[0])
    for i in range(loops(len(points))):
        dist, join = possible.pop(0)
        joined = set()
        for circuit in circuits:
            for point in join:
                if point in circuit:
                    joined |= circuit
        circuits = [x for x in circuits if x&join == set()]
        circuits.append(joined)
    circuits.sort(key = lambda l: len(l), reverse=True)
    print(len(circuits[0]), len(circuits[1]), len(circuits[2]))
    return len(circuits[0])*len(circuits[1])*len(circuits[2])
    pass

def partTwo(input: TextIOWrapper):
    points = []
    possible = []
    for num, line in enumerate(input):
        points.append(tuple([int(s) for s in line.split(",")]))
    circuits = [{y} for y in points]
    for x, point in enumerate(points):
        for y, other in enumerate(points):
            if point is not other and y > x:
                possible.append((distance(point, other), {point, other}))
    possible.sort(key =lambda t: t[0])
    while len(circuits) > 1:
        dist, join = possible.pop(0)
        joined = set()
        for circuit in circuits:
            for point in join:
                if point in circuit:
                    joined |= circuit
        circuits = [x for x in circuits if x&join == set()]
        circuits.append(joined)
        last = list(join)
    return last[0][0]*last[1][0]


    pass

def distance(point1, point2):
    return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2

def loops(total: int):
    if total > 20:
        return total
    else:
        return 10