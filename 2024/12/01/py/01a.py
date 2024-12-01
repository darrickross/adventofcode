#!/usr/bin/env python3

# https://adventofcode.com/2024/day/1

import os

INPUT_FILE_REL_PATH = "../input"


# def read_input(input_file_path: str) -> tuple[list, list]:

#     return (left, right)


def get_difference(a: int, b: int) -> int:
    return abs(a - b)


def main():
    left = []
    right = []

    file_path = os.path.join(os.path.dirname(__file__), INPUT_FILE_REL_PATH)

    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                left.append(int(parts[0]))
                right.append(int(parts[1]))

    left.sort()
    right.sort()
    # difference = []
    total_difference = 0

    for ll, rr in zip(left, right):
        total_difference += get_difference(ll, rr)

    print(total_difference)


if __name__ == "__main__":
    main()
