input, input_moves = open("./day15/input.txt").read().strip().split("\n\n")
grid = [list(row) for row in input.split("\n")]
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

def is_in_bound(x, y):
    return 0 <= x < rows and 0 <= y < cols

def is_empty(x, y):
    return grid[x][y] == '.'

def is_box(x, y):
    return grid[x][y] == 'O'

def is_wall(x, y):
    return grid[x][y] == '#'

def can_move(x, y, dx, dy):
    curr_x, curr_y = x, y
    boxes_to_push = []

    while is_in_bound(curr_x, curr_y):
        if is_wall(curr_x, curr_y):
            return False, []
        elif is_box(curr_x, curr_y):
            boxes_to_push.append((curr_x, curr_y))
        elif is_empty(curr_x, curr_y):
            break

        curr_x += dx
        curr_y += dy

    if not is_in_bound(curr_x, curr_y) or is_wall(curr_x, curr_y):
        return False, []

    return True, boxes_to_push

for mx, my in moves:
    nx, ny = current[0] + mx, current[1] + my

    if is_in_bound(nx, ny) and not is_wall(nx, ny):
        if is_empty(nx, ny):
            grid[current[0]][current[1]] = '.'
            grid[nx][ny] = '@'
            current = (nx, ny)
        elif is_box(nx, ny):
            move, boxes = can_move(nx, ny, mx, my)
            if move:
                for bx, by in reversed(boxes):
                    grid[bx + mx][by + my] = 'O'
                    grid[bx][by] = '.'
                grid[current[0]][current[1]] = '.'
                grid[nx][ny] = '@'
                current = (nx, ny)

image = "\n".join(["".join(row) for row in grid])
print(image)

result = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'O':
            result += 100 * row + col

print(result)
