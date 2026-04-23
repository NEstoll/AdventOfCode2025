from io import TextIOWrapper

def partOne(input: TextIOWrapper):
    points = []
    for line in input:
        points.append(tuple([int(s) for s in line.split(",")]))
    max = 0
    for first in points:
        for second in points:
            area = (abs(first[0]-second[0])+1)*(abs(first[1]-second[1])+1)
            if area > max:
                max = area
    return max
    pass

def partTwo(input: TextIOWrapper):
    points = []
    for line in input:
        points.append(tuple([int(s) for s in line.split(",")]))
    result = 0
    sides = []
    for start, end in zip(points, points[1:]+points[:1]):
        if start[0] == end[0]:
            for k in range(min(start[1], end[1]), max(start[1], end[1])):
                sides.append((start[0], k))
        elif start[1] == end[1]:
            for k in range(min(start[0], end[0]), max(start[0], end[0])):
                sides.append((k, start[1]))
    for i, point in enumerate(points):
        for j, other in enumerate(points):
            if point is other or i>j:
                continue
            area = (abs(point[0]-other[0])+1)*(abs(point[1]-other[1])+1)
            if area <= result:
                continue
            good = True
            for p in sides:
                if (point[0] < p[0] < other[0] or other[0] < p[0] < point[0]) and (point[1] < p[1] < other[1] or other[1] < p[1] < point[1]):
                    good = False
                    break
            if not good:
                continue
            result = area
            # print(point, other, result)
                
            
    return result
    pass

def bad():
    points = []
    for line in input:
        points.append(tuple([int(s) for s in line.split(",")]))
    points.append(points[0])
    result = 0
    fullPoints = []
    for i, point in enumerate(points[:-1]):
        sides = [points[i-1], points[i+1]]
        for first, second in zip(points[:-1], points[1:]):
            if first is point or second is point:
                continue
            if first[0] == second[0] and (first[1] <= point[1] <= second[1] or second[1] <= point[1] <= first[1]):
                sides.append((first[0], point[1]))
            elif first[1] == second[1] and (first[0] <= point[0] <= second[0] or second[0] <= point[0] <= first[0]):
                sides.append((point[0], first[1]))
        minimum = (min(sides, key=lambda a: a[0])[0], min(sides, key=lambda a: a[1])[1])
        maximum = (max(sides, key=lambda a: a[0])[0], max(sides, key=lambda a: a[1])[1])
        fullPoints.append((point, minimum, maximum))
    for point, pointMin, pointMax in fullPoints:
        for other, otherMin, otherMax  in fullPoints:
            if point is not other and pointMin[0] <= other[0] <= pointMax[0] and pointMin[1] <= other[1] <= pointMax[1] and otherMin[0] <= point[0] <= otherMax[0] and otherMin[1] <= point[1] <= otherMax[1]:
                area = (abs(point[0]-other[0])+1)*(abs(point[1]-other[1])+1)
                if area > result:
                    result = area
                    print(point, other, result)
        