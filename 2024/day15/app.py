# app.py
import copy
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from collections import deque

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")

input, input_moves = open("./day15/input.txt").read().strip().split("\n\n")
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

def is_empty(r, c):
    return grid[r][c] == '.'

def is_wall(r, c):
    return grid[r][c] == '#'

def lets_move(curr_r, curr_c, dr, dc):
    pending_moves = set()
    check_cells = deque([(curr_r, curr_c)])

    while check_cells:
        r, c = check_cells.pop()
        if (r, c) in pending_moves:
            continue

        if is_wall(r, c):
            return (curr_r, curr_c)

        if grid[r][c] == "[":
            check_cells.append((r, c+1))

        elif grid[r][c] == "]":
            check_cells.append((r, c-1))

        if not is_empty(r, c):
            pending_moves.add((r, c))
            check_cells.append((r + dr, c + dc))

    new_positions = []
    while pending_moves:
        r, c = pending_moves.pop()
        box = grid[r][c]
        grid[r][c] = '.'
        r += dr
        c += dc
        new_positions.append((r, c, box))

    for r, c, box in reversed(new_positions):
        grid[r][c] = box

    return (curr_r + dr, curr_c + dc)

grids = []
index = 0
for mr, mc in moves:
    index += 1
    current = lets_move(current[0], current[1], mr, mc)
    grid[current[0]][current[1]] = "@"
    # copy only first 1000 steps
    if index < 1000:
        grids.append(copy.deepcopy(grid))

@app.get("/api")
def get_data():
    return {
        "grids": grids,
    }

# todo: figure out how can we keep this common for all days
@app.get("/", response_class=HTMLResponse)
def get_html():
    with open("./day15/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
