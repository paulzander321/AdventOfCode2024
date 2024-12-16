import sys
from pathlib import Path

def solve_part1(data):
    arrangement = [int(element) for element in data.split(" ")]
    for loop in range(25):
        newArrangement = []
        for rockIndex in range(len(arrangement)):
            if arrangement[rockIndex] == 0:
                newArrangement.append(1)
            elif len(str(arrangement[rockIndex])) % 2 == 0:
                rockNumLength = len(str(arrangement[rockIndex]))
                newArrangement.append(int(str(arrangement[rockIndex])[:int(rockNumLength/2)]))
                newArrangement.append(int(str(arrangement[rockIndex])[int(rockNumLength/2):]))
            else:
                newArrangement.append(arrangement[rockIndex] * 2024)
        arrangement = newArrangement.copy()
    return len(arrangement)

def arrangeSplit(arrangement):
    newArrangement = []
    for rockIndex in range(len(arrangement)):
        if arrangement[rockIndex] == 0:
            newArrangement.append(1)
        elif len(str(arrangement[rockIndex])) % 2 == 0:
            rockNumLength = len(str(arrangement[rockIndex]))
            newArrangement.append(int(str(arrangement[rockIndex])[:int(rockNumLength/2)]))
            newArrangement.append(int(str(arrangement[rockIndex])[int(rockNumLength/2):]))
        else:
            newArrangement.append(arrangement[rockIndex] * 2024)
    return newArrangement

def solve_part2(data):
    arrangement = [int(element) for element in data.split(" ")]
    for loop in range(15):
        print("Loop: " + str(loop) + ", Initial Arrangement Count: " + str(len(arrangement)))
        arrangement = arrangeSplit(arrangement)
    return len(arrangement)

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readline()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))