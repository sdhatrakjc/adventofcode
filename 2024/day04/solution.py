directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0), # horizontal and vertical
    (1, 1), (1, -1), (-1, 1), (-1, -1) # diagonal
]

input = []
for line in open("./day04/input.txt"):
    input.append(line.strip())

result = 0
xmas = "XMAS"
rows = len(input)
cols = len(input[0])

def search(row, col, x, y):
    for index in range(4): # XMAS has 4 letters
        m, n = row + index * x, col + index * y
        # row/cols < 0 OR row/cols >= length OR not equal to XMAS
        if  m < 0 or n < 0 or \
            m >= rows or n >= cols or \
            input[m][n] != xmas[index]:
            return False
    return True

for row in range(rows):
    for col in range(cols):
        for x, y in directions:
            if search(row, col, x, y):
                result += 1

print(result)


result = 0
def is_xmas(row, col):
    # always ensure `A` is in the middle
    # this was the key to solve the problem and took me a while to figure out after carefully observing input:/
    # and it simplifies the problem a lot
    if input[row + 1][col + 1] != 'A':
        return False

    diagonal1 = [input[row][col], input[row + 2][col + 2]]
    diagonal2 = [input[row][col + 2], input[row + 2][col]]

    def is_valid_diagonal(diagonal):
            # after checking the input and problem, the count for M and S should be 1 always
            # can't be M-A-M or S-A-S in the same diagonal
            # if diagonal.count('M') == 1 and diagonal.count('S') == 1:
        if 'M' in diagonal and 'S' in diagonal:
            return True

    if is_valid_diagonal(diagonal1) and is_valid_diagonal(diagonal2):
        return True
    else:
        return False

for row in range(rows - 2):
    for col in range(cols - 2):
        if is_xmas(row, col):
            result += 1

print(result)
