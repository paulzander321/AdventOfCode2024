import sys
from pathlib import Path

def solve_part1(data):
    return "hey"


def solve_part2(data):
    return "howdy"

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))