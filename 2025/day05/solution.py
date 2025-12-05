ranges_input, ingredients_input = open("./day05/input.txt").read().strip().split("\n\n")

ranges = []
for line in ranges_input.splitlines():
    a, b = map(int, line.split('-'))
    ranges.append((a, b))

ingredients = [int(x) for x in ingredients_input.splitlines()]

result1 = 0
for ingredient in ingredients:
    for a, b in ranges:
        if a <= ingredient <= b:
            result1 += 1
            break

print(result1)

ranges.sort()
merged = []
current_start, current_end = ranges[0]

for start, end in ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged.append((current_start, current_end))
        current_start, current_end = start, end

merged.append((current_start, current_end))

result2 = 0
for start, end in merged:
    result2 += end - start + 1
print(result2)
