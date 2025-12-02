for line in open('./day02/input.txt'):
    ranges = line.strip().split(',')
    result1 = 0 # sum of invalid IDs
    result2 = 0 # sum of invalid IDs with repeating patterns

    for range_pair in ranges:
        start, end = map(int, range_pair.split('-'))
        for id in range(start, end + 1):
            if len(str(id)) % 2 == 0:  # even length
                first_half = str(id)[:len(str(id)) // 2]
                second_half = str(id)[len(str(id)) // 2:]
                if first_half == second_half:
                    result1 += id

            s = str(id)
            length = len(s)

            for i in range(1, length // 2 + 1):
                if length % i == 0:
                    part = s[:i]
                    if part * (length // i) == s:
                        result2 += id
                        break

    print(result1)
    print(result2)
