grid = [list(line.strip()) for line in open("day04/input.txt")]
rows = len(grid)
cols = len(grid[0])

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def count_neighbors(r, c):
    adjacent = 0
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                adjacent += 1
    return adjacent

result1 = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            if count_neighbors(r, c) < 4:
                result1 += 1
print(result1)



result2 = 0
while True:
    removed = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_neighbors(r, c) < 4:
                    removed.append((r, c))

    if not removed:
        break

    for r, c in removed:
        grid[r][c] = '.'
        result2 += 1

print(result2)
