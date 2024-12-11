# for line in open('./day11/input.txt'):
#     stones = [int(x) for x in line.strip().split()]

# for _ in range(25):
#     result = []
#     for stone in stones:
#         stone_str = str(stone)
#         if stone == 0:
#             result.append(1)
#         elif len(stone_str) % 2 == 0:
#             mid = len(stone_str) // 2
#             a = int(stone_str[:mid])
#             b = int(stone_str[mid:])
#             result.append(a)
#             result.append(b)
#         else:
#             result.append(stone * 2024)
#     stones = result
#     # print(stones)
# print(len(stones))


for line in open('./day11/input.txt'):
    inputs = map(int, line.split())
    stones = {}
    for input in inputs:
        stones[input] = stones.get(input, 0) + 1

for index in range(1, 76):
    result = {}
    for stone, num_stone in stones.items():
        if stone == 0:
            result[1] = result.get(1, 0) + num_stone
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            a, b = int(stone_str[:mid]), int(stone_str[mid:])
            result[a] = result.get(a, 0) + num_stone
            result[b] = result.get(b, 0) + num_stone
        else:
            new_val = 2024 * stone
            result[new_val] = result.get(new_val, 0) + num_stone

    stones = result

    if index == 25 or index == 75:
        print(sum(result.values()))
