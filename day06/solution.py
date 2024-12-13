import sys
import re
from pathlib import Path

def solve_part1(data):
    startX = 0
    startY = 0
    lineCount = len(data)
    lineLength = len(data[0]) - 1
    for line in data:
        if "^" in line:
            startX = data.index(line)
            startY = line.index("^")
    curX = startX
    curY = startY
    curDir = "^"
    travelMap = list(data)
    travelRow = travelMap[curX]
    updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
    travelMap[curX] = updatedRow
    while curX > 0 and curX < lineCount - 1 and curY > 0 and curY < lineLength:
        if curDir == "^":
            if curX - 1 >= 0 and data[curX - 1][curY] == "#":
                curDir = ">"
            else:
                curX -= 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
        elif curDir == ">":
            if curY + 1 <= lineLength and data[curX][curY + 1] == "#":
                curDir = "v"
            else:
                curY += 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
        elif curDir == "<":
            if curY - 1 >= 0 and data[curX][curY - 1] == "#":
                curDir = "^"
            else:
                curY -= 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
        else:
            #down
            if curX + 1 <= lineCount and data[curX + 1][curY] == "#":
                curDir = "<"
            else:
                curX += 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
    travelCount = 0
    for line in travelMap:
        travelCount += len(re.findall("X", line))
    return travelCount


def solve_part2(data):
    startX = 0
    startY = 0
    lineCount = len(data)
    lineLength = len(data[0]) - 1
    for line in data:
        if "^" in line:
            startX = data.index(line)
            startY = line.index("^")
    curX = startX
    curY = startY
    curDir = "^"
    travelMap = list(data)
    travelRow = travelMap[curX]
    updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
    travelMap[curX] = updatedRow
    while curX > 0 and curX < lineCount - 1 and curY > 0 and curY < lineLength:
        if curDir == "^":
            if curX - 1 >= 0 and data[curX - 1][curY] == "#":
                curDir = ">"
            else:
                curX -= 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
        elif curDir == ">":
            if curY + 1 <= lineLength and data[curX][curY + 1] == "#":
                curDir = "v"
            else:
                curY += 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
        elif curDir == "<":
            if curY - 1 >= 0 and data[curX][curY - 1] == "#":
                curDir = "^"
            else:
                curY -= 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
        else:
            #down
            if curX + 1 <= lineCount and data[curX + 1][curY] == "#":
                curDir = "<"
            else:
                curX += 1
                travelRow = travelMap[curX]
                updatedRow = travelRow[:curY] + "X" + travelRow[curY + 1:]
                travelMap[curX] = updatedRow
    travelCount = 0
    for line in travelMap:
        travelCount += len(re.findall("X", line))
    return travelCount

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))