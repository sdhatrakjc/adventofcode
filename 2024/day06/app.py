# app.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = []
start = [0, 0]
with open("./day06/input.txt") as file:
    for xIndex, line in enumerate(file):
        input.append(line.strip())

        for yIndex, char in enumerate(line):
            if char == "^":
                start[0] = xIndex
                start[1] = yIndex
                break

def get_next(position, next_direction):
    return [position[0] + next_direction[0], position[1] + next_direction[1]]

visited_positions = []
turn_positions = []
current = start
direction_index = 0
result = {tuple(start)}

while True:
    next_position = get_next(current, directions[direction_index])

    if (next_position[0] < 0 or next_position[0] >= len(input) or next_position[1] < 0 or next_position[1] >= len(input[0])):
        break

    # right turn
    if input[next_position[0]][next_position[1]] == "#":
        direction_index = (direction_index + 1) % 4
        turn_positions.append(current)
    else:
        visited_positions.append(current)
        current = next_position
        visited_positions.append(current)
        result.add(tuple(current))

@app.get("/api")
def get_data():
    return {
        "input": input,
        "start": start,
        "visited_positions": visited_positions,
        "turn_positions": turn_positions
    }

@app.get("/", response_class=HTMLResponse)
def get_html():
    with open("./day06/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
