import math

def partOne(file):
    sum = 0
    input = file
    for line in input:
        pairs = line.split(",")
        for pair in pairs:
            start, end = pair.split("-")
            for i in range(int(start), int(end)+1):
                cumulative = ""
                for digit in str(i):
                    cumulative += digit
                    if (str(i).count(cumulative)*len(cumulative) == len(str(i))) and str(i).count(cumulative) == 2:
                        sum += i
                        # print(i, " is ", cumulative, str(i).count(cumulative), " times")
                        break
    return sum

def partTwo(file):
    sum = 0
    input = file
    for line in input:
        pairs = line.split(",")
        for pair in pairs:
            start, end = pair.split("-")
            for i in range(int(start), int(end)+1):
                cumulative = ""
                for digit in str(i):
                    cumulative += digit
                    if (str(i).count(cumulative)*len(cumulative) == len(str(i))) and str(i).count(cumulative) > 1:
                        sum += i
                        # print(i, " is ", cumulative, str(i).count(cumulative), " times")
                        break
    return sum        
