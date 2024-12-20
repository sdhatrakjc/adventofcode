import math

# A, B, C = (729, 0, 0)
# program = [0, 1, 5, 4, 3, 0]

A, B, C = (41644071, 0, 0)
program = [2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0]

def get_value(A, B, C):
    output = []
    pointer = 0

    def get_combo(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C

    while pointer < len(program):
        opcode = program[pointer]

        if pointer < len(program):
            operand = program[pointer + 1]
        else:
            operand = 0

        match opcode:
            case 0:
                A = A // (2 ** get_combo(operand))
            case 1:
                B = B ^ operand
            case 2:
                B = get_combo(operand) % 8
            case 3:
                if A != 0:
                    pointer = operand
                    continue
            case 4:
                B = B ^ C
            case 5:
                output.append(get_combo(operand) % 8)
            case 6:
                B = A // (2 ** get_combo(operand))
            case 7:
                C = A // (2 ** get_combo(operand))

        pointer += 2
    return output

print(",".join(map(str, get_value(A, B, C))))

def get_lowest_initial_value(A, B, C):
    queue = [(0, len(program) - 1)]
    min = math.inf

    while len(queue) > 0:
        print('a')
        current_a, position = queue.pop()

        for index in range(8):
            A = current_a + index * 8 ** position

            out = get_value(A, B, C)
            if len(out) > position and out[position] == program[position]:
                if position == 0:
                    if A < min:
                        min = A
                else:
                    queue.append((A, position - 1))
    return min

print(get_lowest_initial_value(A, B, C))
