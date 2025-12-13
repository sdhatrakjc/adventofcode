from itertools import combinations
import timeit
import re

input = open('./day10/input.txt').readlines()

line_regex = re.compile(r"\[([.#]+)\]\s*((?:\([0-9,]*\)\s*)+)\{([^}]*)\}")
button_regex = re.compile(r"\(([0-9,]*)\)")

machines = []
for line in input:
    raw = line_regex.fullmatch(line.strip())

    pattern = raw.group(1)
    buttons_raw = raw.group(2)
    joltage = raw.group(3)

    button_matrix = []
    for button in button_regex.findall(buttons_raw):
        indices = [int(val) for val in button.split(',')] if button else []
        binaries = tuple(1 if index in indices else 0 for index in range(len(pattern)))
        button_matrix.append(binaries)

    target = tuple(int(index) for index in joltage.split(","))

    # print(button_matrix)
    rows = len(button_matrix)
    cols = len(button_matrix[0])

    # all possible combination
    patterns = {}
    for count in range(rows + 1):
        for buttons in combinations(range(rows), count):
            pattern = []
            for i in range(cols):
                total = 0
                for button in buttons:
                    total += button_matrix[button][i]
                pattern.append(total)
            pattern = tuple(pattern)

            if pattern not in patterns:
                patterns[pattern] = len(buttons)
                # print(pattern)

    machines.append((patterns, target))
    # print("---- pattern ----")

def solve_counters(patterns, target):
    cache = {}

    def recurse(target):
        if target in cache:
            return cache[target]

        if all(index == 0 for index in target):
            cache[target] = 0
            return 0

        min_presses = float('inf')

        for pattern, value in patterns.items():
            valid_pattern = True

            for i in range(len(pattern)):
                p = pattern[i]
                t = target[i]

                if not (p <= t and (p & 1) == (t & 1)):
                    valid_pattern = False
                    break

            if valid_pattern:
                new_target = []
                for current, applied in zip(target, pattern):
                    remaining_count = (current - applied) // 2
                    new_target.append(remaining_count)

                new_target = tuple(new_target)

                candidate = value + 2 * recurse(new_target)

                if candidate < min_presses:
                    min_presses = candidate

        cache[target] = min_presses
        return min_presses

    return recurse(target)

start_time = timeit.default_timer()
result = 0
for index, (patterns, target) in enumerate(machines, 1):
    res = solve_counters(patterns, target)
    print(index, res)
    result += res
print(result)
print(f"Execution Time: {timeit.default_timer() - start_time} secs")
