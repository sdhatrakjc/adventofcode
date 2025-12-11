from collections import defaultdict
from itertools import combinations

input = open("./day09/test.txt").readlines()

red_tiles = []
for line in input:
    x, y = map(int, line.strip().split(','))
    red_tiles.append((x, y))

polygon = red_tiles[:]

x_bounds_by_y = defaultdict(list)

length = len(polygon)
for i in range(length):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % length]

    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            x_bounds_by_y[y1].append(x)

    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            x_bounds_by_y[y].append(x1)

for y in x_bounds_by_y:
    xs = x_bounds_by_y[y]
    x_bounds_by_y[y] = (min(xs), max(xs))

def is_rectangle_inside(min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        if y not in x_bounds_by_y:
            return False

        left, right = x_bounds_by_y[y]
        if min_x < left or max_x > right:
            return False

    return True

result2 = 0

for (x1, y1), (x2, y2) in combinations(red_tiles, 2):
    if x1 == x2 or y1 == y2:
        continue

    min_x, max_x = sorted((x1, x2))
    min_y, max_y = sorted((y1, y2))

    if is_rectangle_inside(min_x, max_x, min_y, max_y):
        area = (max_x - min_x + 1) * (max_y - min_y + 1)
        result2 = max(area, result2)

print(result2)
