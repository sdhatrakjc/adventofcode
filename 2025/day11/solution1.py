input = open("./day11/test.txt").readlines()

connections = {}
for line in input:
    start, end = line.strip().split(": ")
    connected_nods = end.strip().split(" ")
    connections[start] = connected_nods

def find_paths(connections, start, end, path=[]):
    path.append(start)

    if start == end:
        return [path]

    if start not in connections:
        return []

    paths = []
    for node in connections[start]:
        if node not in path:
            new_paths = find_paths(connections, node, end, path.copy())
            paths.extend(new_paths)

    return paths

paths = find_paths(connections, "you", "out")
print(len(paths))
