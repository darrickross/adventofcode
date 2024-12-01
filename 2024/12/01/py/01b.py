#!/usr/bin/env python3

# https://adventofcode.com/2024/day/1#part2

import os

INPUT_FILE_REL_PATH = "../input"


# def read_input(input_file_path: str) -> tuple[list, list]:

#     return (left, right)


def get_difference(a: int, b: int) -> int:
    return abs(a - b)


def main():
    left = []
    right = {}

    file_path = os.path.join(os.path.dirname(__file__), INPUT_FILE_REL_PATH)

    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                left.append(int(parts[0]))

                if int(parts[1]) not in right:
                    right[int(parts[1])] = 1
                else:
                    right[int(parts[1])] += 1

    total_similarity = 0

    for ll in left:
        if ll not in right:
            # ll x 0 = 0
            continue

        total_similarity += ll * right[ll]

    print(total_similarity)


if __name__ == "__main__":
    main()
