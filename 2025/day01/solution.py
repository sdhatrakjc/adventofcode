
dial = 50
result1 = 0
result2 = 0
for line in open("./day01/input.txt"):
    direction, count = line.strip()[:1], int(line.strip()[1:])
    # if direction == "L":
    #     dial = (dial - count) % 100
    # else:
    #     dial = (dial + count) % 100

    # if dial == 0:
    #     result1 += 1

    if direction == "L":
        for _ in range(count):
            dial = (dial + 1) % 100
            if dial == 0:
                result2 += 1
    else:
        for _ in range(count):
            dial = (dial - 1) % 100
            if dial == 0:
                result2 += 1

    if dial == 0:
        result1 += 1

print(result1)
print(result2)
