from io import TextIOWrapper


def partOne(input: TextIOWrapper):
    problems = []
    sum = 0
    for line in input:
        l = line.strip().split(" ")
        try:
            l = [int(num) for num in l if num != ""]
        except ValueError:
            l = [num for num in l if num != ""]
        for i, item in enumerate(l):
            if len(problems) <= i:
                problems.append([])
            problems[i].append(item)
    for problem in problems:
        operation = problem.pop()
        match operation:
            case "*":
                total = 1
                for num in problem:
                    total = total * num
                sum += total
            case "+":
                total = 0
                for num in problem:
                    total = total + num
                sum += total
    return sum


def partTwo(input: TextIOWrapper):
    chars = []
    sum = 0
    for line in input:
        c = []
        for char in line.strip("\n"):
            c.append(char)
        chars.append(c)
    operations = [symbol for symbol in chars.pop() if symbol != " "]
    print(operations)
    problem = []
    for i in reversed(range(len(chars[0]))):
        num = ""
        for line in chars:
            num += line[i]
        if (len(num.strip()) == 0):
            operation = operations.pop()
            print(operation.join([str(num) for num in problem]))
            match operation:
                case "*":
                    total = 1
                    for num in problem:
                        total = total * num
                    sum += total
                case "+":
                    total = 0
                    for num in problem:
                        total = total + num
                    sum += total
            problem = []
        else:
            problem.append(int(num))
    operation = operations.pop()
    print(operation.join([str(num) for num in problem]))
    match operation:
        case "*":
            total = 1
            for num in problem:
                total = total * num
            sum += total
        case "+":
            total = 0
            for num in problem:
                total = total + num
            sum += total
    return sum
        
        