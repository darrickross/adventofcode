#!/usr/bin/env python3

# https://adventofcode.com/2024/day/2#part2

import os

INPUT_FILE_REL_PATH = "../input_b"
INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), INPUT_FILE_REL_PATH)

MAX_DIFF = 3
MAX_PROBLEM_DAMPENERS = 1


def is_ascending(a: int, b: int) -> bool:
    if a < b:
        return True
    return False


def validate_rule_2(a: int, b: int) -> bool:
    """
    Test rule 2
    """

    if a == b:
        return False

    if abs(a - b) > MAX_DIFF:
        return False

    return True


def validate_report(_report: list[int]) -> bool:
    if len(_report) < 2:
        return validate_rule_2(_report[0], _report[1])

    assume_list_is_ascending = is_ascending(_report[0], _report[1])
    remaining_problem_dampener = MAX_PROBLEM_DAMPENERS
    last_item_was_skipped = False

    xx = 0
    for ii in range(1, len(_report)):
        is_item_invalid = False

        if not validate_rule_2(_report[ii], _report[xx]):
            # Rule 2
            is_item_invalid = True

        if assume_list_is_ascending:
            if _report[ii] < _report[xx]:
                # This conflicts with the first 2 entries
                # Rule 1: All increasing or decreasing
                is_item_invalid = True
        else:
            if _report[ii] > _report[xx]:
                # This conflicts with the first 2 entries
                # Rule 1: All increasing or decreasing
                is_item_invalid = True

        # Only trigger if one of the above conditions hit meaning we have a bad item
        if is_item_invalid:
            if remaining_problem_dampener <= 0:
                return False

            if ii == 1:
                if len(_report) < 3:
                    return False

                assume_list_is_ascending = is_ascending(_report[0], _report[2])

            remaining_problem_dampener -= 1
            continue
        # continue without updating xx

        # otherwise update xx for next iteration
        xx += 1

    return True


def main():
    file_path = INPUT_FILE_PATH
    count_of_valid_reports = 0

    with open(file_path, "r") as file:
        for line in file:
            report = [int(num) for num in line.split()]

            if validate_report(report):
                count_of_valid_reports += 1

    print(count_of_valid_reports)


if __name__ == "__main__":
    main()
