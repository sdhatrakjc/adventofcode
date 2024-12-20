patterns_in, designs = open('./day19/input.txt').read().strip().split('\n\n')
patterns = patterns_in.split(', ')

def get_design(design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    return dp[n]

result1 = sum(get_design(design) > 0 for design in designs.split('\n'))

result1 = 0
result2 = 0
for design in designs.split('\n'):
    result = get_design(design)
    if result > 0:
        result1 += 1
        result2 += result

print(result1)
print(result2)
