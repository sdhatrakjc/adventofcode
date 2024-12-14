import re

result = 0
for claw in open("./day13/input.txt").read().strip().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", claw))

    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx

    if ca % 1 == cb % 1 == 0:
        if ca <= 100 and cb <= 100:
            result += int(ca*3 + cb)

print(result)

result = 0
for claw in open("./day13/input.txt").read().strip().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", claw))

    px += 10000000000000
    py += 10000000000000

    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx

    if ca % 1 == cb % 1 == 0:
        result += int(ca*3 + cb)

print(result)

