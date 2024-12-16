import sys
from pathlib import Path
import heapq
import math

def print_weighted_map(mazeMap, weights):
    for y in range(len(mazeMap)):
        lineToPrint = ""
        for x in range(len(mazeMap[y])):
            if ((x,y) in weights):
                lineToPrint += f"{weights[(x,y)][0]:4}"
            else:
                lineToPrint += f"{mazeMap[y][x]:4}"
        print(lineToPrint)

def solve_part1(data):
    mazeMap = []
    mazeWeights = {}

    #Parse the data to create maze map and store points
    for y in range(len(data)):
        lineText = data[y].rstrip()
        mazeMap.append(list(lineText))
        for x in range(len(lineText)):
            if lineText[x] == "." or lineText[x] == "S" or lineText[x] == "E":
                mazeWeights[(x, y)] = (float('inf'), "")
                if lineText[x] == "S":
                    startCoord = (x, y)
                elif lineText[x] == "E":
                    targetCoord = (x, y)

    #directions reindeer can move
    directions = {
        "N": (0, -1),
        "S": (0, 1),
        "E": (1, 0),
        "W": (-1, 0)
    }

    #Also defines which directions we can turn
    turn_costs = {
        "N": {"N": 1, "E": 1001, "W": 1001},
        "S": {"S": 1, "E": 1001, "W": 1001},
        "E": {"E": 1, "S": 1001, "N": 1001},
        "W": {"W": 1, "S": 1001, "N": 1001}
    }

    #Initialize start coordinate with weight 0, dir "E"
    mazeWeights[startCoord] = (0, "E")
    best_path = math.inf
    seen = {}
    heap = []
    heapq.heappush(heap, (0, startCoord, "E"))
    while heap:
        current_weight, current_point, current_direction = heapq.heappop(heap)
        x, y = current_point
        if current_weight > mazeWeights[current_point][0]:
            continue
        seen[current_direction, current_point] = True
        for direction, (dx, dy) in directions.items():
            neighbor = (x + dx, y + dy)
            if neighbor in mazeWeights and direction in turn_costs[current_direction]:
                #Calculate the new weight...
                if not (direction, neighbor) in seen:
                    new_weight = current_weight + turn_costs[current_direction][direction]
                    if new_weight < mazeWeights[neighbor][0]:
                        mazeWeights[neighbor] = (new_weight, direction)
                        heapq.heappush(heap, (new_weight, neighbor, direction))

    return mazeWeights[targetCoord][0]


def solve_part2(data):
    return "howdy"

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))