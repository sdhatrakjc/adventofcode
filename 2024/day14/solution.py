# for bigger inputs
rows, cols = 101, 103

# for test input
# rows, cols = 11, 7

robots = []
for line in open("./day14/input.txt"):
    robot = line.strip().split()
    px, py = [int(x) for x in robot[0].strip("p=").split(",")]
    vx, vy = [int(x) for x in robot[1].strip("v=").split(",")]
    robots.append((px, py, vx, vy))

quadrants = [0, 0, 0, 0]
mx, my = rows // 2, cols // 2
for px, py, vx, vy in robots:
    npx = (px + vx * 100) % rows
    npy = (py + vy * 100) % cols

    if npx < mx:
        if npy < my:
            quadrants[0] += 1
        elif npy > my:
            quadrants[1] += 1
    elif npx > mx:
        if npy < my:
            quadrants[2] += 1
        elif npy > my:
            quadrants[3] += 1

result = 1
for x in quadrants:
    result *= x
print(result)

for sec in range(1, 10000):
    new_robots = []
    grid = [['.'] * rows for _ in range(cols)]

    for px, py, vx, vy in robots:
        npx = (px + vx) % rows
        npy = (py + vy) % cols
        new_robots.append((npx, npy, vx, vy))
        grid[npy][npx] = '*'

    image = "\n".join("".join(tile) for tile in grid)
    # print(image)
    if '*******************************' in image:
        print(image)
        print(sec)

    robots = new_robots
