def perform_operation(nums, operator):
    if operator == "*":
        total = 1
        for n in nums:
            total *= n
    elif operator == "+":
        total = sum(nums)
    return total

worksheet = open('./day06/input.txt').read().strip("\n")

lines = worksheet.split("\n")
height = len(lines)
length = max(len(row) for row in lines)

lines = [line + " " * (length - len(line)) for line in lines]

separator = []
for c in range(length):
    if all(lines[r][c] == " " for r in range(height)):
        separator.append(True)
    else:
        separator.append(False)

blocks = []
start = None

for c in range(length):
    if not separator[c]:
        if start is None:
            start = c
    else:
        if start is not None:
            blocks.append((start, c))
            start = None

if start is not None:
    blocks.append((start, length))

result1 = []
result2 = []
for (a, b) in blocks:
    width = b - a
    block = [line[a:b] for line in lines]
    block = [row for row in block if row.strip()]
    operator = block[-1].strip()

    # PART 1
    nums1 = []
    for row in block[:-1]:
        nums1.append(int(row.strip()))

    answer = perform_operation(nums1, operator)
    result1.append(answer)

    # PART 2
    nums2 = []
    for c in reversed(range(width)):
        digits = ''.join(block[r][c] for r in range(height - 1)).strip()

        if digits:
            nums2.append(int(digits))

    answer = perform_operation(nums2, operator)
    result2.append(answer)

print(sum(result1))
print(sum(result2))
