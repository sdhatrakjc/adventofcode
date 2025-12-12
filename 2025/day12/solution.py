input = open('./day12/test.txt').read().strip().split('\n\n')

presents = []
for line in input[:-1]:
    presents.append(line.split('\n')[1:])

shapes = []
for line in input[-1].split('\n'):
    shapes.append(line.split(' '))

result = 0
for line in shapes:
    sizes = []
    for val in line[0][:-1].split('x'):
        sizes.append(int(val))

    size = sizes[0]*sizes[1]

    indexes = line[1:]

    sp = 0
    for index, val in enumerate(indexes):
        a = presents[index]
        sa = ''.join(a).count('#')
        sp += int(val) * sa

    diff = size-sp
    if diff > 0:
        result += 1

print(result)
