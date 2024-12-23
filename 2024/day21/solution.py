from collections import deque

codes = open('./day21/input.txt').read().strip().split('\n')

directions = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['-', '0', 'A']
]

controller = [
    ['-', '^', 'A'],
    ['<', 'v', '>']
]

def get_shortest_path(start, end, grid):
    queue = deque([(start, '')])
    visited = set()
    shortest_paths = []
    min_length = float('inf')

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            if len(path) < min_length:
                min_length = len(path)
                shortest_paths = [path + 'A']
            elif len(path) == min_length:
                shortest_paths.append(path + 'A')
            continue

        visited.add((r, c))

        for dir, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc

            if  not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue

            if (nr, nc) not in visited and grid[nr][nc] != '-':
                queue.append(((nr, nc), path + dir))

    return shortest_paths

def get_sequence(code, grid):
    sequences = ['']

    for i in range(-1, len(code)-1):
        if i == -1:
            S, E = 'A', code[i + 1]
        else:
            S, E = code[i], code[i + 1]

        start, end = (0, 0), (0, 0)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == S:
                    start = row, col
                if grid[row][col] == E:
                    end = row, col

        paths = get_shortest_path(start, end, grid)
        sequences = [s + path for s in sequences for path in paths]

    return sequences

result = 0
for code in codes:
    keys = get_sequence(code, keypad)

    controller_sequences = []
    for key in keys:
        intermediate_sequences = get_sequence(key, controller)
        controller_sequences.extend(intermediate_sequences)

    final_sequences = []
    for sequence in controller_sequences:
        shortest_sequences = get_sequence(sequence, controller)
        final_sequences.extend(shortest_sequences)

    complexity = len(min(final_sequences, key=len)) * int(code[:3])
    result += complexity

print(result)

# def calculate_complexity():
#     total_complexity = 0

#     for code in codes:
#         keys = get_sequence(code, keypad)

#         for i in range(25):
#             new_keys = []
#             for key in keys:
#                 robot_sequence = get_sequence(key, controller)
#                 new_keys.extend(robot_sequence)
#             keys = new_keys

#         final_sequence = get_sequence(keys[0], keypad)[0]

#         numeric_part = int(code[:-1])
#         total_complexity += len(final_sequence) * numeric_part

#     return total_complexity

# print(calculate_complexity())
