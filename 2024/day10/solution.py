input = []
for line in open('./day10/input.txt'):
    trails = [int(x) for x in line.strip()]
    input.append(trails)

rows, cols = len(input), len(input[0])
# print(input)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_trails(x, y):
    peaks = set()
    all_paths = set()

    def dfs(x, y, step, path):
        if step == 9:
            peaks.add((x, y))
            all_paths.add(tuple(path))
            return

        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if (0 <= newX < rows and 0 <= newY < cols and input[newX][newY] == step + 1):
                new_path = path + [(newX, newY)]
                # print(new_path)
                dfs(newX, newY, step + 1, new_path)

    dfs(x, y, 0, [(x, y)])
    return len(peaks), len(all_paths)

result1 = 0
result2 = 0
for xIndex in range(rows):
    for yIndex in range(cols):
        if input[xIndex][yIndex] == 0:
            total_peaks, unique_trails = get_trails(xIndex, yIndex)
            result1 += total_peaks
            result2 += unique_trails

print(result1)
print(result2)
