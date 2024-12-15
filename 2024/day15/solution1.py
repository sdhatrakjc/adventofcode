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

def is_in_bound(r, c):
    return 0 <= r < rows and 0 <= c < cols

def is_empty(r, c):
    return grid[r][c] == '.'

def is_box(r, c):
    return grid[r][c] == 'O'

def is_wall(r, c):
    return grid[r][c] == '#'

def can_move(r, c, dr, dc):
    curr_r, curr_c = r, c
    boxes_to_push = []

    while is_in_bound(curr_r, curr_c):
        if is_wall(curr_r, curr_c):
            return False, []
        elif is_box(curr_r, curr_c):
            boxes_to_push.append((curr_r, curr_c))
        elif is_empty(curr_r, curr_c):
            break

        curr_r += dr
        curr_c += dc

    if not is_in_bound(curr_r, curr_c) or is_wall(curr_r, curr_c):
        return False, []

    return True, boxes_to_push

for mr, mc in moves:
    nr, nc = current[0] + mr, current[1] + mc

    if is_in_bound(nr, nc) and not is_wall(nr, nc):
        if is_empty(nr, nc):
            grid[current[0]][current[1]] = '.'
            grid[nr][nc] = '@'
            current = (nr, nc)
        elif is_box(nr, nc):
            move, boxes = can_move(nr, nc, mr, mc)
            if move:
                for br, bc in reversed(boxes):
                    grid[br + mr][bc + mc] = 'O'
                    grid[br][bc] = '.'
                grid[current[0]][current[1]] = '.'
                grid[nr][nc] = '@'
                current = (nr, nc)

image = "\n".join(["".join(cell) for cell in grid])
print(image)

result = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'O':
            result += 100 * row + col

print(result)
