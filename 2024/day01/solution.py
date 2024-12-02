list1 = []
list2 = []
for line in open("./day01/input.txt"):
    numbers = line.strip().split("   ")
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

list1 = sorted(list1)
list2 = sorted(list2)

result1 = sum(abs(a - b) for a, b in zip(list1, list2))
print(result1)

result2 = 0
for val in list1:
    count = list2.count(val)
    result2 += count * val

print(result2)
