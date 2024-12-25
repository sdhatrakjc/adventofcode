lockHeights = []
keyHeights = []

inputs = open("./day25/input.txt").read().split('\n\n')
for input in inputs:
	grid = input.strip().split('\n')
	heights = []

	if input[0][0] == "#":
		for c in range(len(grid[0])):
			height = 0
			for r in range(1, len(grid)):
				if grid[r][c] == "#":
					height += 1
			heights.append(height)
		lockHeights.append(heights)

	elif input[0][0] == ".":
		for c in range(len(grid[0])):
			height = 0
			for r in range(len(grid)-1):
				if grid[r][c] == "#":
					height += 1
			heights.append(height)
		keyHeights.append(heights)

result = 0
for lock in lockHeights:
	for key in keyHeights:
		overlap = False
		for i in range(5):
			if lock[i] + key[i] > 5:
				overlap = True
				break
		if not overlap:
			result += 1
print(result)
