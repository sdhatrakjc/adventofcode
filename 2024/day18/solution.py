from collections import deque

rows, cols = 71, 71

# rows, cols = 7, 7

positions = []
for line in open("./day18/input.txt"):
    x, y = [int(x) for x in line.strip().split(",")]
    positions.append((x, y))

grid = [["." for _ in range(cols)] for _ in range(rows)]

for x, y in positions[:1024]:
    if 0 <= x < cols and 0 <= y < rows:
        grid[y][x] = "#"

# image = "\n".join(["".join(row) for row in grid])
# print(image)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, start, end):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in visited and grid[ny][nx] == ".":
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))

    return -1

start = (0, 0)
end = (cols - 1, rows - 1)

steps = bfs(grid, start, end)
print(steps)

def is_path_to_exit(grid, start, end):
    queue = deque([start])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return True

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == ".":
                queue.append((nx, ny))

    return False

grid = [["." for _ in range(cols)] for _ in range(rows)]
for idx, (x, y) in enumerate(positions):
    if 0 <= x < cols and 0 <= y < rows:
        grid[y][x] = "#"
        if not is_path_to_exit(grid, start, end):
            print(f"{x},{y}")
            break
