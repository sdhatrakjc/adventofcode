import heapq

grid = []
for line in open("./day16/input.txt"):
    row = [cell for cell in line.strip()]
    grid.append(row)

directions = [
    (-1, 0, 'N'),
    (1, 0, 'S'),
    (0, -1, 'W'),
    (0, 1, 'E')
]

rows, cols = len(grid), len(grid[0])

start = (0, 0)
end = (0, 0)

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            start = (r, c)
        if grid[r][c] == "E":
            end = (r, c)

def get_result():
    priority_queue = [(0, start[0], start[1], 'E')]
    visited = set()

    while priority_queue:
        cost, r, c, dir = heapq.heappop(priority_queue)

        if (r, c) == end:
            return cost

        if (r, c, dir) in visited:
            continue

        visited.add((r, c, dir))

        for dr, dc, new_dir in directions:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == '#':
                continue

            move_cost = 1
            if dir != new_dir:
                rotation_cost = 1000
            else:
                rotation_cost = 0
            new_cost = cost + move_cost + rotation_cost

            heapq.heappush(priority_queue, (new_cost, nr, nc, new_dir))

    return -1

print(get_result())

def get_result2():
    priority_queue = [(0, start[0], start[1], 'E', [(start[0], start[1])])]
    visited = dict()
    min_cost = float('inf')
    tiles = set()

    while priority_queue:
        cost, r, c, dir, path = heapq.heappop(priority_queue)

        if cost > min_cost:
            continue

        if (r, c) == end:
            if cost <= min_cost:
                min_cost = cost
                tiles = tiles.union(set(path))
            # return cost

        if (r, c, dir) in visited and visited[(r, c, dir)] < cost:
            continue

        visited[((r, c, dir))] = cost

        for dr, dc, new_dir in directions:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == '#':
                continue

            move_cost = 1
            if dir != new_dir:
                rotation_cost = 1000
            else:
                rotation_cost = 0
            new_cost = cost + move_cost + rotation_cost

            heapq.heappush(priority_queue, (new_cost, nr, nc, new_dir, path + [(nr, nc)]))

    # print(tiles)
    return tiles

tiles = get_result2()
# for r, row in enumerate(grid):
#     for c, char in enumerate(row):
#         if (r, c) in tiles:
#             grid[r][c] = 'O'

# print('\n'.join([''.join(row) for row in grid]))
print(len(tiles))
