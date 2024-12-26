from functools import cache

codes = open('./day21/input.txt').read().strip().split('\n')

keypad = {
    '7':0,
    '8':1,
    '9':2,
    '4':1j,
    '5':1+1j,
    '6':2+1j,
    '1':2j,
    '2':1+2j,
    '3':2+2j,
    '-':3j,
    '0':1+3j,
    'A':2+3j,
}

controller = {
    '-':0,
    '^':1,
    'A':2,
    '<':1j,
    'v':1+1j,
    '>':2+1j,
}

# Ref- https://will-keleher.com/posts/2d-navigation-with-imaginary-numbers-is-better.html
# elegant way to calculate the path between two points in a 2D grid by using complex numbers
@cache
def get_path(start, end):
    grid = keypad if start in keypad and end in keypad else controller
    start_position, end_position = grid[start], grid[end]
    diff = end_position - start_position
    dx, dy = int(diff.real), int(diff.imag)

    vertical_moves = "^" * -dy if dy < 0 else "v" * dy
    horizontal_moves = "<" * -dx if dx < 0 else ">" * dx

    obstacle_diff = grid["-"] - start_position
    prioritize_vertical = (dx > 0 or obstacle_diff == dx) and obstacle_diff != dy * 1j

    result = (vertical_moves + horizontal_moves if prioritize_vertical else horizontal_moves + vertical_moves) + "A"
    # print(start, end, result)
    return result

    
@cache
def length(code, depth):
    result = 0
    if depth == 0: return len(code)
    for index, char in enumerate(code):
        result += length(get_path(code[index-1], char), depth-1)
    return result


result1 = sum(int(code[:-1]) * length(code, 3) for code in codes)
print(result1)

result2 = sum(int(code[:-1]) * length(code, 26) for code in codes)
print(result2)

# MOVES -
# 7-A = >>vvvA
# 7-0 = >vvvA
# 7-1 = vvA
# 7-2 = >vvA
# 7-3 = >>vvA
# 7-4 = vA
# 7-5 = v>A
# 7-6 = v>>A
# 7-7 = A
# 7-8 = >A
# 7-9 = >>A

# 8-A = vvv>A
# 8-0 = vvvA
# 8-1 = <vvA
# 8-2 = vvA
# 8-3 = vv>A
# 8-4 = <vA
# 8-5 = vA
# 8-6 = v>A
# 8-7 = <A
# 8-8 = A
# 8-9 = >A

# 9-A = vvvA
# 9-0 = <vvvA
# 9-1 = <<vvA
# 9-2 = <vvA
# 9-3 = vvA
# 9-4 = <<vA
# 9-5 = <vA
# 9-6 = vA
# 9-7 = <<A
# 9-8 = <A
# 9-9 = A

# 4-A = >>vvA
# 4-0 = >vvA
# 4-1 = vA
# 4-2 = v>A
# 4-3 = >>vA
# 4-4 = A
# 4-5 = >A
# 4-6 = >>A
# 4-7 = ^A
# 4-8 = ^>A
# 4-9 = ^>>A

# 5-A = vv>A
# 5-0 = vvA
# 5-1 = <vA
# 5-2 = vA
# 5-3 = v>A
# 5-4 = <A
# 5-5 = A
# 5-6 = >A
# 5-7 = <^A
# 5-8 = ^A
# 5-9 = ^>A

# 6-A = vvA
# 6-0 = <vvA
# 6-1 = <<vA
# 6-2 = <vA
# 6-3 = vA
# 6-4 = <<A
# 6-5 = <A
# 6-6 = A
# 6-7 = <<^A
# 6-8 = <^A
# 6-9 = ^A

# 1-A = >>vA
# 1-0 = >vA
# 1-1 = A
# 1-2 = >A
# 1-3 = >>A
# 1-4 = ^A
# 1-5 = ^>A
# 1-6 = ^>>A
# 1-7 = ^^A
# 1-8 = ^^>A
# 1-9 = ^^>>A

# 2-A = v>A
# 2-0 = vA
# 2-1 = <A
# 2-2 = A
# 2-3 = >A
# 2-4 = <^A
# 2-5 = ^A
# 2-6 = ^>A
# 2-7 = <^^A
# 2-8 = ^^A
# 2-9 = ^^>A

# 3-A = vA
# 3-0 = v<A
# 3-1 = <<A
# 3-2 = <A
# 3-3 = A
# 3-4 = <<^A
# 3-5 = <^A
# 3-6 = ^A
# 3-7 = <<^^A
# 3-8 = <^^A
# 3-9 = ^^A

# 0-A = >A
# 0-1 = ^<A
# 0-2 = ^A
# 0-3 = ^>A
# 0-4 = ^^<A
# 0-5 = ^^A
# 0-6 = ^^>A
# 0-7 = ^^^<A
# 0-8 = ^^^A
# 0-9 = >^^^A

# A-0 = <A
# A-1 = ^<<A
# A-2 = <^A
# A-3 = ^A
# A-4 = ^^<<A
# A-5 = <^^A
# A-6 = ^^A
# A-7 = ^^^<<A
# A-8 = <^^^A
# A-9 = ^^^A

# A-< = v<<A
# A-v = <vA
# A-> = vA
# A-^ = <A
# ^-A >A
# ^-< v<A
# ^-^ A
# ^-> v>A
# <-A >>^A
# <-< = A
# <-^ = >^A
# <-v = >A
# = v-A = ^>A
# v-v = A
# v-> = >A
# v-< = <A
# = >-^ = <^A
# >-A = ^A
# >-> = A
# >-v = <A
