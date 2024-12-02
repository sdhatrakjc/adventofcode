def is_report_safe(levels):
    order = 0  # 0: ascending, 1: descending
    if levels[1] < levels[0]:
        order = 1

    for prev, curr in zip(levels, levels[1:]):
        if not (1 <= abs(curr - prev) <= 3):
            return False
        if order == 1 and curr > prev:
            return False
        elif order == 0 and curr < prev:
            return False
    return True

def is_report_safe_with_tolerance(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_report_safe(modified_levels):
            return True
    return False

safe = 0
updated_safe = 0
for report in open("./day02/input.txt"):
    levels = [int(level) for level in report.strip().split(' ')]
    if is_report_safe(levels):
        safe += 1
    if is_report_safe(levels) or is_report_safe_with_tolerance(levels):
        updated_safe += 1
print(safe)
print(updated_safe)
