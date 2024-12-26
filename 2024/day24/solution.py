import re
from collections import defaultdict

initial_values = {}
gates = []
gates_dict = {}

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
        gates_dict[out] = (in1, op, in2)
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
z_values = [z_wires[f"z{i:02}"] for i in range(len(z_wires))]
binary_nums = "".join(map(str, reversed(z_values)))
print(int(binary_nums, 2))


# x = x01, y = y01
# AND(x, y) -> and_gate[0]
# XOR(x, y) -> xor_gate[0]
# z01 = XOR(xor_gate[0], carry[0]) -> z_gate[0]
# If z01 does not match expected wire z01, swap gates.
# Repeat for each i, until correct.
# For each gate, check if the current conf matches the target, swap wires if mismatch.

and_gates = [None] * 45
xor_gates = [None] * 45
z_gates = [None] * 45
temp_gates = [None] * 45
carry_gates = [None] * 45

swapped_wires = []
i = 0
x_wire = "x" + str(i).zfill(2)
y_wire = "y" + str(i).zfill(2)

def similar_gate(in1, opr, in2):
    for output_wire, (i1, op, i2) in gates_dict.items():
        if (in1, opr, in2) in [(i1, op, i2), (i2, op, i1)]:
            return output_wire
    return None

and_gates[i] = similar_gate(x_wire, "AND", y_wire)
xor_gates[i] = similar_gate(x_wire, "XOR", y_wire)
z_gates[i] = xor_gates[i]
carry_gates[i] = and_gates[i]

def swap_wires(wire1, wire2, swapped_wires):
    gates_dict[wire1], gates_dict[wire2] = gates_dict[wire2], gates_dict[wire1]
    swapped_wires += [wire1, wire2]

for i in range(1, 45):
    x_wire = "x" + str(i).zfill(2)
    y_wire = "y" + str(i).zfill(2)
    z_wire = "z" + str(i).zfill(2)

    needs_swap = True
    while needs_swap:
        needs_swap = False
        and_gates[i] = similar_gate(x_wire, "AND", y_wire)
        xor_gates[i] = similar_gate(x_wire, "XOR", y_wire)

        in1, op, in2 = gates_dict[z_wire]
        if in1 == carry_gates[i - 1] and in2 != xor_gates[i]:
            swap_wires(in2, xor_gates[i], swapped_wires)
            needs_swap = True
            continue
        if in2 == carry_gates[i - 1] and in1 != xor_gates[i]:
            swap_wires(in1, xor_gates[i], swapped_wires)
            needs_swap = True
            continue

        z_gates[i] = similar_gate(xor_gates[i], "XOR", carry_gates[i - 1])
        if z_gates[i] != z_wire:
            swap_wires(z_gates[i], z_wire, swapped_wires)
            needs_swap = True
            continue

        temp_gates[i] = similar_gate(xor_gates[i], "AND", carry_gates[i - 1])
        carry_gates[i] = similar_gate(temp_gates[i], "OR", and_gates[i])

# print(swapped_wires)

result = ",".join(sorted(swapped_wires))
print(result)
