from io import TextIOWrapper
from itertools import combinations

def partOne(input: TextIOWrapper):
    tries = 0
    for line in input:
        components = line.split(" ")
        goal = [[c=='#' for c in x[1:-1]] for x in components if x.startswith("[") and x.endswith("]")][0]
        buttons = [list(map(lambda s: int(s), x[1:-1].split(","))) for x in components if x.startswith("(") and x.endswith(")")]
        voltage = [list(map(lambda s: int(s), x[1:-1].split(","))) for x in components if x.startswith("{") and x.endswith("}")]
        total, sequence = computeLights(goal, [False for x in goal], buttons)
        tries += total
    return tries
    pass

def partTwo(input: TextIOWrapper): #got 16853
    tries = 0
    for line in input:
        components = line.rstrip().split(" ")
        goal = [[c=='#' for c in x[1:-1]] for x in components if x.startswith("[") and x.endswith("]")][0]
        buttons = [list(map(lambda s: int(s), x[1:-1].split(","))) for x in components if x.startswith("(") and x.endswith(")")]
        voltage = [list(map(lambda s: int(s), x[1:-1].split(","))) for x in components if x.startswith("{") and x.endswith("}")][0]
        # current = [0 for x in voltage]
        # best = 0
        # queue = []
        # while current != voltage:
        #     for button in buttons:
        #         queue.append((best+1, [x+(i in button) for i, x in enumerate(current)]))
        #     queue = [(x, y) for x, y in queue if len([h for h, m in zip(y, voltage) if h>m])==0]
        #     best, current = queue.pop(0)
        # tries += best
        # print("computing for", voltage)
        total = computeVoltage(voltage, buttons)
        print(total)
        tries += total
    return tries
    pass


voltageCalls = {}
def computeVoltage(goal: list[int],  buttons: list[list[int]]) -> int:
    if goal == [0 for x in goal]:
        # print("found solution")
        return 0
    if voltageCalls.get(str(goal)) is not None and voltageCalls.get(str(goal)).get(str(buttons)) is not None:
        return voltageCalls[str(goal)][str(buttons)]
    if len([y for y in goal if y<0]) != 0:
        return -1
    best = -1
    parity = [x%2==1 for x in goal]
    new_var = computeCombos(parity, [0 for x in goal], buttons)
    for total, presses in new_var:
        new = [(x-sum([i in button for button in presses]))//2 for i, x in enumerate(goal)]
        recurse = computeVoltage(new, buttons)
        if recurse != -1 and (best == -1 or (recurse*2 + total) < best):
            best = recurse*2 + total
    # buttons.sort(reverse=True, key=lambda x: len(x))
    # for button in buttons:
    #     if best != -1 and len(ideal[-1]) > len(button):
    #         continue
    #     new = [x+(i in button) for i, x in enumerate(current)]
    #     total, presses = computeVoltage(goal, new, buttons)
    #     if total != -1 and (best == -1 or total+1 < best):
    #         best = total+1
    #         ideal = presses+[button]
    if voltageCalls.get(str(goal)) is None:
        voltageCalls[str(goal)] = {}
    voltageCalls[str(goal)][str(buttons)] = best
    return best

comboCalls = {}
def computeCombos(goal: list[bool], current: list[bool], buttons: list[list[int]]) -> list[tuple[int, list[list[int]]]]:
    if comboCalls.get(str(goal)) is not None and comboCalls.get(str(goal)).get(str(current)) is not None and comboCalls.get(str(goal)).get(str(current)).get(str(buttons)) is not None:
        return comboCalls[str(goal)][str(current)][str(buttons)]
    combos = []
    if goal == current:
        combos += [(0, [])]
    used = []
    for button in buttons:
        used.append(button)
        new = [(i in button) ^ x for i, x in enumerate(current)]
        result = computeCombos(goal, new, [x for x in buttons if x not in used])
        combos += [(total+1, presses+[button]) for total, presses in result]
    if comboCalls.get(str(goal)) is None:
        comboCalls[str(goal)] = {}
    if comboCalls[str(goal)].get(str(current)) is None:
        comboCalls[str(goal)][str(current)] = {}
    comboCalls[str(goal)][str(current)][str(buttons)] = combos
    return combos

lightsCalls = {}
def computeLights(goal: list[bool], current: list[bool], buttons: list[list[int]]) -> tuple[int, list[list[int]]]:
    if goal == current:
        return (0, [])
    if lightsCalls.get(str(goal)) is not None and lightsCalls.get(str(goal)).get(str(current)) is not None and lightsCalls.get(str(goal)).get(str(current)).get(str(buttons)) is not None:
        return lightsCalls[str(goal)][str(current)][str(buttons)]
    best = -1
    ideal = [[-1]]
    for button in buttons:
        new = [(i in button) ^ x for i, x in enumerate(current)]
        total, presses = computeLights(goal, new, [x for x in buttons if x is not button])
        if best == -1 or total+1 < best:
            best = total+1
            ideal = presses+[button]
    if lightsCalls.get(str(goal)) is None:
        lightsCalls[str(goal)] = {}
    if lightsCalls[str(goal)].get(str(current)) is None:
        lightsCalls[str(goal)][str(current)] = {}
    lightsCalls[str(goal)][str(current)][str(buttons)] = (best, ideal)
    return (best, ideal)