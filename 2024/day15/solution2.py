from collections import deque

input, input_moves = open("./day15/test.txt").read().strip().split("\n\n")
old_grid = [list(row) for row in input.split("\n")]
grid = []
for row in old_grid:
    new_row = []
    for cell in row:
        if cell == "@":
            new_row.append(cell)
            new_row.append(".")
            continue
        elif cell == "O":
            new_row.append("[")
            new_row.append("]")
            continue
        new_row.append(cell)
        new_row.append(cell)
    grid.append(new_row)

moves_string = input_moves.replace("\n", "")

dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}
moves = []
for move in moves_string:
    moves.append(dirs[move])

current = (0, 0)
rows, cols = len(grid), len(grid[0])
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "@":
            current = row, col
            break

def is_empty(x, y):
    return grid[x][y] == '.'

def is_wall(x, y):
    return grid[x][y] == '#'

def lets_move(curr_x, curr_y, dx, dy):
    pending_moves = set()
    check_cells = deque([(curr_x, curr_y)])

    while check_cells:
        x, y = check_cells.pop()
        if (x, y) in pending_moves:
            continue

        if is_wall(x, y):
            return (curr_x, curr_y)

        if grid[x][y] == "[":
            check_cells.append((x, y+1))

        elif grid[x][y] == "]":
            check_cells.append((x, y-1))

        if not is_empty(x, y):
            pending_moves.add((x, y))
            check_cells.append((x + dx, y + dy))

    new_positions = []
    while pending_moves:
        x, y = pending_moves.pop()
        box = grid[x][y]
        grid[x][y] = '.'
        x += dx; y += dy
        new_positions.append((x, y, box))

    for x, y, box in reversed(new_positions):
        grid[x][y] = box

    return (curr_x + dx, curr_y + dy)

for mx, my in moves:
    current = lets_move(current[0], current[1], mx, my)

image = "\n".join(["".join(row) for row in grid])
print(image)

result = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "[":
            result += 100 * i + j

print(result)
