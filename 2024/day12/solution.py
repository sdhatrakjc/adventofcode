directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
input = []
for line in open('./day12/input.txt'):
    input.append([x for x in line.strip()])

rows, cols = len(input), len(input[0])

# dfs
def get_regions():
    visited = set()
    regions = []

    def dfs(x, y, plant):
        # out of bound
        if (x < 0 or x >= rows or
            y < 0 or y >= cols or
            (x, y) in visited or
            input[x][y] != plant):
            return set()

        region = {(x, y)}
        visited.add((x, y))

        for dx, dy in directions:
            region.update(dfs(x + dx, y + dy, plant))

        return region

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:
                region = dfs(x, y, input[x][y])
                if region:
                    regions.append(region)

    return regions

def calculate_perimeter(region):
    perimeter = 0
    plant = input[next(iter(region))[0]][next(iter(region))[1]]
    # print(plant)

    for x, y in region:
        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if (newX < 0 or newX >= rows or
                newY < 0 or newY >= cols or
                input[newX][newY] != plant):
                perimeter += 1
    # print(perimeter)
    return perimeter

from collections import defaultdict

def calculate_sides(region):
    horizontal = set()
    vertical = set()

    for x, y in region:
        # top
        if y+1 >= cols or (x, y+1) not in region:
            vertical.add((x, y, directions[0]))

        # bottom
        if y-1 < 0 or (x, y-1) not in region:
            vertical.add((x, y, directions[2]))

        # right
        if x+1 >= rows or (x+1, y) not in region:
            horizontal.add((x, y, directions[1]))

        # left
        if x-1 < 0 or (x-1, y) not in region:
            horizontal.add((x, y, directions[3]))

    # print(horizontal)
    # print(vertical)

    updated_horizontals = set()
    updated_verticals = set()

    each_row = defaultdict(list)
    # x is constant for each row
    for x, y, dir in sorted(horizontal):
        each_row[(x, dir)].append(y)
    # print(by_row)

    # idea here is to merge the entire side if it has same x and direction
    for (x, dir), y_points in each_row.items():
        y_points.sort()
        current = y_points[0]
        prev = current

        for y in y_points[1:]:
            if y > prev + 1:
                updated_horizontals.add((x, current, prev, dir))
                current = y
            prev = y
        updated_horizontals.add((x, current, prev, dir))
    # print(merged_h)

    each_col = defaultdict(list)
    for x, y, dir in sorted(vertical):
        each_col[(y, dir)].append(x)

    for (y, dir), x_points in each_col.items():
        x_points.sort()
        current = x_points[0]
        prev = current

        for x in x_points[1:]:
            if x > prev + 1:
                updated_verticals.add((y, current, prev, dir))
                current = x
            prev = x
        updated_verticals.add((y, current, prev, dir))

    return len(updated_horizontals) + len(updated_verticals)

result1 = 0
result2 = 0
regions = get_regions()
# print(len(regions))

for region in regions:
    area = len(region)
    perimeter = calculate_perimeter(region)
    sides = calculate_sides(region)
    price1 = area * perimeter
    price2 = area * sides
    result1 += price1
    result2 += price2
    # break
print(result1)
print(result2)
