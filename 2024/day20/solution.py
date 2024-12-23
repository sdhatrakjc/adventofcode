from collections import deque, defaultdict

grid = open("./day20/input.txt").read().strip().split("\n")

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            start = (r, c)
        if grid[r][c] == 'E':
            end = (r, c)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_total():
    queue = deque()
    queue.append((end, 0))
    visited = set()

    path = [end]
    steps_dict = {end: 1}

    while queue:
        curr, steps = queue.popleft()
        visited.add(curr)

        if curr == start:
            path.reverse()
            return steps_dict, path

        for d in directions:
            nr, nc = curr[0] + d[0], curr[1] + d[1]

            if not 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                continue

            if grid[nr][nc] in 'S.' and (nr, nc) not in visited:
                steps_dict[(nr, nc)] = steps + 1
                queue.append(((nr, nc), steps + 1))
                path.append((nr, nc))

def get_result():
    queue = deque()
    queue.append((start, 1, False))
    visited = set()

    counts = defaultdict(int)
    steps_dict, path = find_total()
    total = len(steps_dict)

    while queue:
        curr, steps, jumped = queue.popleft()
        for d in directions:
            nr, nc = curr[0] + d[0], curr[1] + d[1]

            if not 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                continue

            if grid[nr][nc] in 'E.' and (nr, nc) not in visited:
                if jumped:
                    saved = total - (steps + steps_dict[(nr, nc)]) - 1
                    counts[saved] += 1
                else:
                    queue.append(((nr, nc), steps + 1, jumped))
                    visited.add((nr, nc))
            elif grid[nr][nc] == '#' and not jumped:
                queue.append(((nr, nc), steps, True))

    return sum(counts[i] for i in counts if i >= 100), steps_dict, path


result2 = 0
result1, steps_dict, path = get_result()

for i in range(len(path)):
    for j in range(i + 1, len(path)):
        diff = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
        if diff <= 20:
            first, second = steps_dict[path[i]], steps_dict[path[j]]
            saved = first - second - diff
            if saved >= 100:
                result2 += 1

print(result1)
print(result2)
