import re
from itertools import combinations
from collections import deque
from scipy.optimize import milp, LinearConstraint
import numpy as np
import timeit

input = open('./day10/input.txt').readlines()

line_regex = re.compile(r"\[([.#]+)\]\s*((?:\([0-9,]*\)\s*)+)\{([^}]*)\}")
button_regex = re.compile(r"\(([0-9,]*)\)")

machines = []
for line in input:
    raw = line_regex.fullmatch(line.strip())

    pattern = raw.group(1)
    buttons_raw = raw.group(2)
    joltage = raw.group(3)

    buttons = []
    for button in button_regex.findall(buttons_raw):
        if button == "":
            buttons.append([])
        else:
            buttons.append([int(x) for x in button.split(",")])

    machines.append((pattern, buttons, joltage))

def get_pattern_binary(pattern):
    mask = 0
    for i, c in enumerate(pattern):
        if c == "#":
            mask |= (1 << i)
    return mask

def get_button_binary(btn):
    mask = 0
    for i in btn:
        mask |= (1 << i)
    return mask

# PART 1
def solve_pattern(pattern, buttons):
    target_binary = get_pattern_binary(pattern)
    button_binaries = [get_button_binary(b) for b in buttons]
    total_buttons = len(buttons)

    for presses in range(total_buttons + 1):
        for combo in combinations(range(total_buttons), presses):
            state = 0
            for index in combo:
                state ^= button_binaries[index]

            if state == target_binary:
                return presses

    print("some error occured")
    return

result1 = 0
for pattern, buttons, joltage in machines:
    result1 += solve_pattern(pattern, buttons)

print(result1)

# PART 2
def solve_counters_slow(joltage, buttons):
    target = tuple(map(int, joltage.split(",")))

    start = tuple([0]*len(target))
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        state, presses = queue.popleft()
        if state == target:
            return presses

        for button in buttons:
            new_state = list(state)
            for counter in button:
                new_state[counter] += 1
                if new_state[counter] > target[counter]:
                    break
            else:
                new_state = tuple(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, presses + 1))


    print("some error occured")
    return

def solve_counters(joltage, buttons):
    target = np.asarray(list(map(int, joltage.split(","))))
    button_count = len(buttons)

    button_matrix = np.zeros((len(target), button_count))

    for i, button in enumerate(buttons):
        for counter in button:
            button_matrix[counter][i] = 1

    c = np.ones(button_count)

    constraint = LinearConstraint(button_matrix, target, target)
    result = milp(c, integrality=[1]*button_count, constraints=[constraint])

    if result.success:
        return round(result.fun)
    else:
        print("not expected!")
        return

result2 = 0
start_time = timeit.default_timer()

for index, (pattern, buttons, joltage) in enumerate(machines):
    # print(index)
    result2 += solve_counters(joltage, buttons)

print(result2)
print(f"{timeit.default_timer() - start_time} seconds")
