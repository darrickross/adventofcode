#!/usr/bin/env python3

# https://adventofcode.com/2024/day/2

import os

INPUT_FILE_REL_PATH = "../input"
INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), INPUT_FILE_REL_PATH)

MAX_DIFF = 3


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

    assume_ascending = True

    if _report[0] > _report[1]:
        assume_ascending = False

    for ii in range(1, len(_report)):
        if not validate_rule_2(_report[ii], _report[ii - 1]):
            # Rule 2
            return False

        if assume_ascending:
            if _report[ii] < _report[ii - 1]:
                # This conflicts with the first 2 entries
                # Rule 1: All increasing or decreasing
                return False
        else:
            if _report[ii] > _report[ii - 1]:
                # This conflicts with the first 2 entries
                # Rule 1: All increasing or decreasing
                return False

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
