from itertools import product

# do this only from left to right, this makes the problem easier
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        elif operators[i-1] == '|':
            result = int(str(result) + str(numbers[i]))
    return result

# we did this after submitting the problem, so we don't need itertools but is it better ?
# todo: to check if itertools product is doing the same thing or better
def get_combinations(operators, length):
    if length == 0:
        return [[]]
    else:
        combinations = []
        for operator in operators:
            for combination in get_combinations(operators, length - 1):
                combinations.append([operator] + combination)
        return combinations


def can_be_true(test_value, numbers):
    # using `|` for `||` operator mentioned in the problem statement to generate all posibilities and it's combinations
    # itertools came to the rescue from last year's AoC learning.
    # todo: we can create a custom function to generate this
    # for operators in product('+*|', repeat=len(numbers)-1):
    for operators in get_combinations('+*', len(numbers)-1):
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

result = 0
for line in open("./day07/input.txt"):
    value, numbers = line.strip().split(':')
    value = int(value)
    numbers = list(map(int, numbers.split()))
    if can_be_true(value, numbers):
        result += value
print(result)



