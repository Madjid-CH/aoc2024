def parse_input(input_):
    if len(input_) == 0:
        return []
    reports = []
    for line in input_.splitlines():
        reports.append(parse_line(line))
    return reports


def parse_line(line):
    line = line.split(" ")
    return [int(level) for level in line]


def is_safe(report):
    return is_strictly_monotonic(report) and no_gap_bigger_then_3(report)


def no_gap_bigger_then_3(report):
    return check_report(report, lambda x, y: abs(x - y) > 3)


def is_strictly_monotonic(report):
    strictly_increasing = check_report(report, lambda x, y: x <= y)
    strictly_decreasing = check_report(report, lambda x, y: x >= y)
    return strictly_decreasing or strictly_increasing


def check_report(report, failing_criteria):
    for i in range(len(report) - 1):
        if failing_criteria(report[i], report[i + 1]):
            return False
    return True


def count_safe_reports(input_):
    reports = parse_input(input_)
    return sum(is_safe(report) for report in reports)


def count_safe_reports_with_dampener(input_):
    reports = parse_input(input_)
    return sum(is_safe_with_dampener(report) for report in reports)


def is_safe_with_dampener(report: list):
    if r := is_safe(report):
        return r

    for i, _ in enumerate(report):
        dampened_report = report.copy()
        dampened_report.pop(i)
        if r := is_safe(dampened_report):
            return r

    return False


if __name__ == "__main__":
    with open("input", "r") as f:
        print(count_safe_reports_with_dampener(f.read()))
