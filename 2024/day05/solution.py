input = []
seperator = 0
with open("./day05/input.txt") as file:
    for index, line in enumerate(file):
        input.append(line.strip())
        if line.strip() == '':
            seperator = index
rules = input[:seperator]
page_numbers = input[seperator+1:]

def is_valid_order(list, rules):
    pages = [int(x) for x in list]
    for rule in rules:
        before, after = map(int, rule.split('|'))
        if before in pages and after in pages:
            index_1 = pages.index(before)
            index_2 = pages.index(after)
            if index_1 >= index_2:
                return False
    return True

# mimick the return behavior of string comparison
def compare_pages(x, y, rules):
    for rule in rules:
        before, after = map(int, rule.split('|'))
        if x == before and y == after:
            return -1
        if x == before and y == after:
            return 1
    return 0

# just perform a normal sort on the pages
def sort_pages(list, rules):
    pages = [int(x) for x in list]
    n = len(pages)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare_pages(pages[j], pages[j+1], rules) > 0:
                pages[j], pages[j+1] = pages[j+1], pages[j]
    return pages

result1 = 0
result2 = 0
for list in page_numbers:
    list = list.split(',')
    page_length = len(list)

    if is_valid_order(list, rules):
        middle = int(list[page_length // 2])
        result1 += middle
    else:
        sorted_list = sort_pages(list, rules)
        middle = int(sorted_list[page_length // 2])
        result2 += middle

print(result1)
print(result2)
