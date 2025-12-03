import sys
import importlib

def solveSingle(input, output, solve):
    print()
    with open(input, "r") as example:
        result = solve(example)
        print("Ran", getattr(solve, '__name__', 'Unknown'), "on", input, "got\033[1m", result, "\033[0m")
        if output != None:
            with open(output, "r") as expected:
                out = expected.read()
                if (str(result)==out.strip()):
                    print("\033[92mThis matches the expected\033[1m", out, "\033[0m")
                else:
                    print("\033[91mThis doesn't match the expected\033[1m", out, "\033[0m")
        else:
            print("No expected given")
    print()

def solveDay(directory, part1, part2):
    print("Advent of Code 2025", directory)
    solveSingle(directory+"/example.txt", directory+"/expected1.txt", part1)
    solveSingle(directory+"/input.txt", None, part1)
    solveSingle(directory+"/example.txt", directory+"/expected2.txt", part2)
    solveSingle(directory+"/input.txt", None, part2)

day = importlib.import_module(sys.argv[1]+"."+sys.argv[1])

solveDay(sys.argv[1], day.partOne, day.partTwo)

    