from io import TextIOWrapper

def partOne(input: TextIOWrapper):
    devices = {}
    for line in input:
        name = line.split(":")[0]
        outputs = line.split(":")[1].strip().split(" ")
        devices[name] = outputs
    return findPaths(devices, "you", "out")

def partTwo(input: TextIOWrapper):
    devices = {}
    for line in input:
        name = line.split(":")[0]
        outputs = line.split(":")[1].strip().split(" ")
        devices[name] = outputs
    return findPaths2(devices, "svr", "out", False, False)

def findPaths(connections: dict[str, list[str]], start:str, end:str):
    if start == end:
        return 1
    total = 0
    for output in connections[start]:
        total += findPaths(connections, output, end)
    return total

calls = {}
def findPaths2(connections: dict[str, list[str]], start:str, end:str, dac, fft):
    if start == end:
        return dac and fft
    new_var = calls.get(str(connections), {}).get(start, {}).get(end, {}).get(dac, {}).get(fft)
    if new_var is not None:
        return new_var
    total = 0
    for output in connections[start]:
        total += findPaths2(connections, output, end, dac or start=="dac", fft or start=="fft")
    if calls.get(str(connections)) is None:
        calls[str(connections)] = {}
    if calls[str(connections)].get(start) is None:
        calls[str(connections)][start] = {}
    if calls[str(connections)][start].get(end) is None:
        calls[str(connections)][start][end] = {}
    if calls[str(connections)][start][end].get(dac) is None:
        calls[str(connections)][start][end][dac] = {}
    if calls[str(connections)][start][end][dac].get(fft) is None:
        calls[str(connections)][start][end][dac][fft] = total
    return total

