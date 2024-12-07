# app.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from itertools import product

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

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

def get_combinations(operators, length):
    if length == 0:
        return [[]]
    else:
        combinations = []
        for operator in operators:
            for combination in get_combinations(operators, length - 1):
                combinations.append([operator] + combination)
        return combinations


def get_opeators(test_value, numbers):
    for operators in product('+*|', repeat=len(numbers)-1):
        if evaluate_expression(numbers, operators) == test_value:
            return True, operators
    return False, []

values = []
numbers = []
operators = []
result = 0
results = []
for line in open("./day07/input.txt"):
    a, b = line.strip().split(':')
    value = int(a)
    values.append(value)

    nums = list(map(int, b.split()))
    numbers.append(nums)

    process, ops = get_opeators(value, nums)
    operators.append(ops)
    if process:
        result += value

    results.append(result)
# print(result)

@app.get("/api")
def get_data():
    return {
        "numbers": numbers,
        "operators": operators,
        "values": values,
        "results": results
    }

# todo: figure out how can we keep this common for all days
@app.get("/", response_class=HTMLResponse)
def get_html():
    with open("./day07/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
