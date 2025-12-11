input = open("./day11/input.txt").readlines()

connections = {}
for line in input:
    start, end = line.strip().split(": ")
    connected_nods = end.strip().split(" ")
    connections[start] = connected_nods

cache = {}
def count(start, end):
    if (start, end) in cache:
        return cache[(start, end)]

    if start == end:
        return 1

    if start not in connections:
        return 0

    total = 0
    for path in connections[start]:
        total += count(path, end)

    cache[(start, end)] = total
    return total

path1 = count("svr", "dac") * count("dac", "fft") * count("fft", "out")
path2 = count("svr", "fft") *  count("fft", "dac") * count("dac", "out")

print(path1 + path2)
