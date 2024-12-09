input = ""
for line in open('./day09/input.txt'):
    input = line.strip()

file = []
fileID = 0
isEmpty = False
for char in input:
    for i in range(0, int(char)):
        if isEmpty:
            file.append(-1)
        else:
            file.append(fileID)

    if isEmpty:
        fileID += 1
    isEmpty = not isEmpty

first = 0
last = len(file) - 1
while first <= last:
    while file[first] >= 0:
        first += 1
    while file[last] < 0:
        last -= 1

    if first < last:
        file[first], file[last] = file[last], file[first]
        # first += 1
        # last -= 1

checksum = 0
for index, val in enumerate(file):
    if val >= 0:
        checksum += index * val
print(checksum) # part1

isEmpty = False
empty = []
files = {}
position = 0

# 2333133121414131402
# empty values: [(2, 3), (8, 3), (12, 3) ...]
# file values: {0: (0, 2), 1: (5, 3), 2: (11, 1) ...}
for index, val in enumerate(input):
    if isEmpty:
        empty.append((position, int(val)))
    else:
        files[len(files)] = (position, int(val))
    position += int(val)
    isEmpty = not isEmpty
# print(empty)
# print(files)

# start filling the empty values with the files from the end
for index in range(len(files) - 1, -1, -1):
    for eIndex, emp in enumerate(empty):
        if emp[0] > files[index][0]:
            break

        size = files[index][1]
        if emp[1] >= size:
            files[index] = (emp[0], size)
            empty[eIndex] = (emp[0] + size, emp[1] - size)
            break

# print(files)
checksum = 0
for file in files:
    position, size = files[file]
    for index in range(size):
        checksum += file * (position + index)
print(checksum) # part2
