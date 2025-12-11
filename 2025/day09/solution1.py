from itertools import combinations

input = open("./day09/input.txt").readlines()

red_tiles = []
for line in input:
    x, y = map(int, line.strip().split(','))
    red_tiles.append((x, y))

result1 = 0
largest_pair = None

for a, b in combinations(range(len(red_tiles)), 2):
    x1, y1 = red_tiles[a]
    x2, y2 = red_tiles[b]

    if x1 != x2 and y1 != y2:
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height

        result1 = max(area, result1)

print(result1)
