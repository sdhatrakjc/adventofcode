import re
from collections import defaultdict

initial_values = {}
gates = []

for line in open("./day24/input.txt"):
    if line.strip() == "":
        continue
    if ":" in line.strip():
        wire, value = line.split(": ")
        initial_values[wire] = int(value)
    else:
        gates.append(line.strip())

values = defaultdict(lambda: None, initial_values)

def solve(gate):
    match = re.match(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)", gate)
    if match:
        in1, op, in2, out = match.groups()
        if values[in1] is None or values[in2] is None:
            return False

        match op:
            case "AND":
                values[out] = values[in1] & values[in2]
            case "OR":
                values[out] = values[in1] | values[in2]
            case "XOR":
                values[out] = values[in1] ^ values[in2]

        return True

pending_gates = gates.copy()
while pending_gates:
    for gate in pending_gates.copy():
        if solve(gate):
            pending_gates.remove(gate)

z_wires = {key: value for key, value in values.items() if key.startswith("z")}
z_actual = [z_wires[f"z{i:02}"] for i in range(len(z_wires))]
binary_nums = "".join(map(str, reversed(z_actual)))
print(int(binary_nums, 2))


