from itertools import combinations

input = []
for line in open('./day08/input.txt'):
    x, y, z = map(int, line.strip().split(","))
    input.append((x, y, z))

length = len(input)

pairs = []
for a, b in combinations(range(length), 2):
    x1, y1, z1 = input[a]
    x2, y2, z2 = input[b]
    dist = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
    pairs.append((dist, a, b))

pairs.sort()

# PART 1
root = list(range(length))

def get_root(node):
    if node != root[node]:
        root[node] = get_root(root[node])
    return root[node]

for _, a, b in pairs[:1000]:
    na, nb = get_root(a), get_root(b)
    root[nb] = na
# print(root)

root_counts = {}
for i in range(length):
    r = get_root(i)
    if r not in root_counts:
        root_counts[r] = 0
    root_counts[r] += 1

sizes = sorted(root_counts.values(), reverse=True)

result1 = sizes[0] * sizes[1] * sizes[2]
print(result1)


# PART 2
root = list(range(length))
num_circuits = length

for _, a, b in pairs:
    na, nb = get_root(a), get_root(b)
    if na == nb:
        continue
    root[nb] = na
    num_circuits -= 1

    if num_circuits == 1:
        x1, x2 = input[a][0], input[b][0]
        result2 = x1 * x2
        print(result2)
        break
