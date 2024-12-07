# up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = []
start = [0, 0]
with open("./day06/input.txt") as file:
    for xIndex, line in enumerate(file):
        input.append(line.strip())

        for yIndex, char in enumerate(line):
            if char == "^":
                start[0] = xIndex
                start[1] = yIndex
                break

def get_next(position, next_direction):
    return [position[0] + next_direction[0], position[1] + next_direction[1]]

visited = {tuple(start)}
current = start
direction_index = 0
while True:
    next_position = get_next(current, directions[direction_index])

    if (next_position[0] < 0 or next_position[0] >= len(input) or next_position[1] < 0 or next_position[1] >= len(input[0])):
        break

    if input[next_position[0]][next_position[1]] == "#":
        direction_index = (direction_index + 1) % 4
    else:
        current = next_position
        visited.add(tuple(current))

result = len(visited)
print(result)


def is_a_loop(started_at):
    visited = set()
    current = list(start)
    direction_index = 0

    while True:
        state = (tuple(current), direction_index)
        if state in visited:
            return True

        visited.add(state)
        next_position = get_next(current, directions[direction_index])

        if (next_position[0] < 0 or next_position[0] >= len(input) or next_position[1] < 0 or next_position[1] >= len(input[0])):
            return False

        if (input[next_position[0]][next_position[1]] == "#" or
            [next_position[0], next_position[1]] == started_at):
            direction_index = (direction_index + 1) % 4
        else:
            current = next_position

loops = set()
# for x in range(len(input)):
#     for y in range(len(input[0])):
#         if [x, y] is start or input[x][y] == "#":
#             continue
#         if is_a_loop([x, y]):
#             loops.add((x, y))

# we can use entire input but there's no point in doing that because loop can happen only in the visited places
# above expensive code can be replaced with below if we only use visited places
for x, y in visited:
    if is_a_loop([x, y]):
        loops.add((x, y))

result2 = len(loops)
print(result2)
