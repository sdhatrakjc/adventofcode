input = open("./day07/input.txt").read().strip().splitlines()

grid = []
for rows in input:
    r = []
    for c in range(0, len(rows)):
        r.append(rows[c])
    grid.append(r)


rows = len(grid)
cols = len(grid[0])

start = grid[0].index("S")
grid[1][start] = "|"

# PART 1
result1 = 0
for r in range(1, rows-1):
    for c in range(cols):
        if grid[r][c] == "|":
            if grid[r+1][c] == "^":
                result1 += 1
                grid[r+1][c-1] = "|"
                grid[r+1][c+1] = "|"
            else:
                grid[r+1][c] = "|"

# [print("".join(row)) for row in grid]
print(result1)

# PART 2
dp = [[0]*cols for _ in range(rows)]
dp[1][start] = 1
for r in range(1, rows-1):
    for c in range(cols):
        if dp[r][c] > 0:
            if grid[r+1][c] == "^":
                if c-1 >= 0:
                    dp[r+1][c-1] += dp[r][c]
                if c+1 < cols:
                    dp[r+1][c+1] += dp[r][c]
            else:
                dp[r+1][c] += dp[r][c]

result2 = sum(dp[rows-1])
print(result2)
