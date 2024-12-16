import sys
from pathlib import Path

DIRECTIONS = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0)
}

def attempt_move(direction, curPos, warehouseMap, piece):
    x, y = curPos
    dx, dy = DIRECTIONS[direction]
    if warehouseMap[y + dy][x + dx] == "#":
        #wall
        return (x, y)
    elif warehouseMap[y + dy][x + dx] == ".":
        warehouseMap[y][x] = "."
        warehouseMap[y + dy][x + dx] = piece
        return (x + dx, y + dy)
    elif warehouseMap[y + dy][x + dx] == "O":
        rock_moved = attempt_move(direction, (x + dx, y + dy), warehouseMap, "O")
        if rock_moved != (x + dx, y + dy):
            #Move allowed
            warehouseMap[y][x] = "."
            warehouseMap[y + dy][x + dx] = piece
            return (x + dx, y + dy)
        else:
            return (x, y)
    else:
        #Default return current position (no move allowed)
        return (x, y)

def solve_part1(data):
    #Parse the data to create warehouse map
    gpsSum = 0
    warehouseMap = []
    robotMoves = []
    roboCoord = (0,0)
    for y in range(len(data)):
        if data[y][0] == "#":
            lineText = data[y].rstrip()
            warehouseMap.append(list(lineText))
            for x in range(len(lineText)):
                if lineText[x] == "@":
                    roboCoord = (x, y)
        elif data[y][0].rstrip() != "":
            robotMoves.extend(list(data[y].rstrip()))
    
    print(roboCoord)

    #Process the robot movements
    for move in robotMoves:
        x, y = roboCoord
        roboCoord = attempt_move(move, roboCoord, warehouseMap, "@")

    #Calculate the coordinate sum
    for y in range(len(warehouseMap)):
        stringToPrint = ""
        for x in range(len(warehouseMap[y])):
            stringToPrint += str(warehouseMap[y][x])
            if warehouseMap[y][x] == "O":
                gpsSum += (y * 100) + x
        print(stringToPrint)

    print(roboCoord)

    return gpsSum

def attempt_big_move(direction, curPos, warehouseMap, piece):
    x, y = curPos
    

    return (curPos)

def solve_part2(data):
    #Parse the data to create warehouse map
    gpsSum = 0
    warehouseMap = []
    robotMoves = []
    roboCoord = (0,0)
    for y in range(len(data)):
        if data[y][0] == "#":
            lineText = data[y].rstrip()
            resizedText = ""
            for x in range(len(lineText)):
                if lineText[x] == "#":
                    resizedText += "##"
                elif lineText[x] == "O":
                    resizedText += "[]"
                elif lineText[x] == ".":
                    resizedText += ".."
                elif lineText[x] == "@":
                    resizedText += "@."
            if "@" in resizedText:
                roboCoord = (resizedText.index("@"), y)
            warehouseMap.append(list(resizedText))
        elif data[y][0].rstrip() != "":
            robotMoves.extend(list(data[y].rstrip()))

    for move in robotMoves:
        roboCoord = attempt_big_move(move, roboCoord, warehouseMap, "@")

    #Calculate the coordinate sum
    for y in range(len(warehouseMap)):
        stringToPrint = ""
        for x in range(len(warehouseMap[y])):
            stringToPrint += str(warehouseMap[y][x])
            if warehouseMap[y][x] == "O":
                gpsSum += (y * 100) + x
        print(stringToPrint)

    return gpsSum

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    # print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))