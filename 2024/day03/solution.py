def update_results(result, line):
    # todo: use regex to get all matches instead
    parts = line.strip().split("mul(")
    for part in parts:
       if part.find(")") >= 1 and len(part.split(")")[0].split(",")) == 2:
            a, b = part.split(")")[0].split(",")
            try:
                result += int(a) * int(b)
            except ValueError:
                pass
    return result

result = 0
for line in open("./day03/input.txt"):
    result += update_results(0, line)
print(result) #part 1

import re
result = 0
current_action = True  # 0 = do, 1 = don't
for line in open("./day03/input.txt"):
    instructions = re.split(r"(do\(\)|don't\(\))", line)
    for instruction in instructions:
        if instruction.startswith("do()"):
            current_action = True
        elif instruction.startswith("don't()"):
            current_action = False
        elif current_action:
            result += update_results(0, instruction)
print(result) #part 2

