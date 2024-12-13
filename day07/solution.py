import sys
from pathlib import Path
from enum import Enum


def isEquationValid(targetTotal, curTotal, nums, curPos):
    if curTotal == targetTotal and curPos == len(nums) - 1:
        return True
    elif curPos == len(nums) - 1:
        return False
    elif curTotal > targetTotal:
        return False
    else:
        return (
                isEquationValid(targetTotal, curTotal + nums[curPos + 1], nums, curPos + 1) or 
                isEquationValid(targetTotal, curTotal * nums[curPos + 1], nums, curPos + 1)
            )
    
def isEquationValidWithConcat(targetTotal, curTotal, nums, curPos):
    if curTotal == targetTotal and curPos == len(nums) - 1:
        return True
    elif curPos == len(nums) - 1:
        return False
    elif curTotal > targetTotal:
        return False
    else:
        return (
                isEquationValidWithConcat(targetTotal, curTotal + nums[curPos + 1], nums, curPos + 1) or
                isEquationValidWithConcat(targetTotal, curTotal * nums[curPos + 1], nums, curPos + 1) or 
                isEquationValidWithConcat(targetTotal, int(str(curTotal) + str(nums[curPos + 1])), nums, curPos + 1)
            )

def solve_part1(data):
    grandTotal = 0
    for line in data:
        lineSplit = line.rstrip().split(":")
        targetTotal = int(lineSplit[0])
        numbers = [int(ele) for ele in lineSplit[1].lstrip().split(" ")]
        if isEquationValid(targetTotal, numbers[0], numbers, 0):
            grandTotal += targetTotal
    return grandTotal


def solve_part2(data):
    grandTotal = 0
    for line in data:
        lineSplit = line.rstrip().split(":")
        targetTotal = int(lineSplit[0])
        numbers = [int(ele) for ele in lineSplit[1].lstrip().split(" ")]
        if isEquationValidWithConcat(targetTotal, numbers[0], numbers, 0):
            grandTotal += targetTotal
    return grandTotal

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))