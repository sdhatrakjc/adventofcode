# app.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from itertools import product

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

# for bigger inputs
rows, cols = 101, 103

robots = []
for line in open("./day14/input.txt"):
    robot = line.strip().split()
    px, py = [int(x) for x in robot[0].strip("p=").split(",")]
    vx, vy = [int(x) for x in robot[1].strip("v=").split(",")]
    robots.append((px, py, vx, vy))

positions = []
for sec in range(1, 10000):
    new_robots = []
    grid = [['.'] * rows for _ in range(cols)]

    for px, py, vx, vy in robots:
        npx = (px + vx) % rows
        npy = (py + vy) % cols
        new_robots.append((npx, npy, vx, vy))
        grid[npy][npx] = '*'

    # do it only for couple of frames because we know the answer :)
    if 7010 < sec < 7040:
        positions.append(new_robots) #position of each robot at each second

    image = "\n".join("".join(tile) for tile in grid)
    # print(image)
    if '*******************************' in image:
        # print(image)
        # print(sec)
        break

    robots = new_robots

@app.get("/api")
def get_data():
    return {
        "positions": positions,
    }

# todo: figure out how can we keep this common for all days
@app.get("/", response_class=HTMLResponse)
def get_html():
    with open("./day14/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
