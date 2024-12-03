import sys
from pathlib import Path

def solve_part1(data):
    listLeft = []
    listRight = []
    for line in data:
        lineSplit = line.split()
        listLeft.append(int(lineSplit[0]))
        listRight.append(int(lineSplit[1]))

    listLeft.sort()
    listRight.sort()

    distanceSum = 0

    for i in range(len(listLeft)):
        distanceSum += abs(listLeft[i] - listRight[i])

    return distanceSum


def solve_part2(data):
    listLeft = []
    listRight = []
    for line in data:
        lineSplit = line.split()
        listLeft.append(int(lineSplit[0]))
        listRight.append(int(lineSplit[1]))

    similarityScore = 0
    for num in listLeft:
        similarityScore += num * listRight.count(num)

    return similarityScore



if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))