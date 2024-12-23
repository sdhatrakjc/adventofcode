inputs = [int(line.strip()) for line in open("./day22/input.txt")]

def get_secrets(secret):
    modulo = 16777216
    secrets = [secret]

    for _ in range(2000):
        secret = (secret ^ (secret * 64)) % modulo
        secret = (secret ^ (secret // 32)) % modulo
        secret = (secret ^ (secret * 2048)) % modulo
        secrets.append(secret)

        # print(secret)
    return secrets

# get_secrets(123)

result1 = 0 # sum of last secrets
result2 = 0 # max_bananas
price_map = {}

for input in inputs:
    secrets = get_secrets(input)
    result1 += secrets[-1]
    prices = [secret % 10 for secret in secrets]
    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

    seen = {}

    for index in range(len(changes) - 3):
        sequence = tuple(changes[index:index + 4])

        if sequence not in seen:
            seen[sequence] = True
            price_map[sequence] = price_map.get(sequence, 0) + prices[index + 4]

            if price_map[sequence] > result2:
                result2 = price_map[sequence]

print(result1)
print(result2)
