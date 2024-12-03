import sys
import re
from pathlib import Path

def solve_part1(data):
    grandTotal = 0
    memoryParsed = []
    for line in data:
        memoryParsed.extend(re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line))

    for term in memoryParsed:
        multTerms = re.findall("[0-9]{1,3}", term)
        if len(multTerms) == 2:
            grandTotal += int(multTerms[0]) * int(multTerms[1])
    return grandTotal


def solve_part2(data):
    grandTotal = 0
    memoryParsed = []
    for line in data:
        memoryParsed.extend(re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)", line))

    keepAdding = True
    for term in memoryParsed:
        if term == "do()":
            keepAdding = True
        elif term == "don't()":
            keepAdding = False
        elif keepAdding:
            multTerms = re.findall("[0-9]{1,3}", term)
            if len(multTerms) == 2:
                grandTotal += int(multTerms[0]) * int(multTerms[1])
    
    return grandTotal


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))