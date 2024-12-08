input = []
antennas = []

with open("./day08/input.txt") as file:
    for xIndex, line in enumerate(file):
        input.append(line.strip())
        for yIndex, char in enumerate(line.strip()):
            if char != ".":
                antennas.append((char, xIndex, yIndex))

rows = len(input)
cols = len(input[0])

result1 = set()
for i, antenna1 in enumerate(antennas):
    for j, antenna2 in enumerate(antennas):
        if i >= j:
            continue

        a1, x1, y1 = antenna1
        a2, x2, y2 = antenna2

        if a1 != a2:
            continue

        # reflection1
        newX1, newY1 = 2*x1 - x2, 2*y1 - y2
        if 0 <= newX1 < rows and 0 <= newY1 < cols:
            result1.add((newX1, newY1))

        # reflection2
        newX2, newY2 = 2*x2 - x1, 2*y2 - y1
        if 0 <= newX2 < rows and 0 <= newY2 < cols:
            result1.add((newX2, newY2))

print(len(result1))


result2 = set()
for i, antenna1 in enumerate(antennas):
    for j, antenna2 in enumerate(antennas):
        if i >= j:
            continue

        a1, x1, y1 = antenna1
        a2, x2, y2 = antenna2

        if a1 != a2:
            continue

        result2.add((x1, y1))
        result2.add((x2, y2))

        # check if they are in the same line and update result
        for x3 in range(rows):
            for y3 in range(cols):
                # slope ? y2-y1 / x2-x1 = y3-y1 / x3-x1
                # if (y2 - y1) / (x2 - x1) == (y3 - y1) / (x3 - x1): (ZeroDivisionError: division by zero)
                # ^ small change made a differnce
                if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                    result2.add((x3, y3))
print(len(result2))
