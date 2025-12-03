result1 = 0
result2 = 0

# this is remove k-digit problem varient
def max_value(bank, num_batteries=12):
    length = len(bank)
    batteries = []
    start = 0

    for _ in range(num_batteries):
        end = length - (num_batteries - len(batteries)) + 1
        max_digit = max(bank[start:end])
        index = bank.index(max_digit, start, end)
        batteries.append(max_digit)
        start = index + 1

    return int(''.join(batteries))

for line in open('./day03/input.txt'):
    bank = line.strip()
    largest_joltage = 0

    largest_digit = -1
    largest_index = 0
    for index in range(len(bank) - 1):
        if int(bank[index]) > largest_digit:
            largest_digit = int(bank[index])
            largest_index = index

    for index in range(largest_index + 1, len(bank)):
        pair_value = int(str(largest_digit) + bank[index])
        if pair_value > largest_joltage:
            largest_joltage = pair_value

    result1 += largest_joltage
    # result1 += max_value(bank, 2) - we can use this for part 1 as well
    result2 += max_value(bank, 12)

print(result1)
print(result2)
