import sys
from pathlib import Path

def solve_part1(data):
    trailheadsTotalScore = 0
    for y in range(len(data)):
        for x in range(len(data[y].rstrip())):
            if data[y][x] == '0':
                #Trailhead
                waveCoordinates = {(x, y)}
                nextWaveCoordinates = set()
                stepCount = 0
                while len(waveCoordinates) > 0 and stepCount < 9:
                    stepCount += 1
                    for coord in waveCoordinates:
                        #up
                        if (coord[1] - 1 >= 0 and data[coord[1]-1][coord[0]] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0],coord[1]-1))

                        #down
                        if (coord[1] + 1 < len(data) and data[coord[1]+1][coord[0]] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0],coord[1]+1))

                        #left
                        if (coord[0] - 1 >= 0 and data[coord[1]][coord[0]-1] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0]-1,coord[1]))

                        #right
                        if (coord[0] + 1 < len(data[y].rstrip()) and data[coord[1]][coord[0]+1] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0]+1,coord[1]))

                    waveCoordinates = nextWaveCoordinates.copy()
                    nextWaveCoordinates.clear()

                #Add wave coordinate count as this trailhead score
                trailheadsTotalScore += len(waveCoordinates)
    return trailheadsTotalScore


def solve_part2(data):
    trailheadsTotalScore = 0
    for y in range(len(data)):
        for x in range(len(data[y].rstrip())):
            if data[y][x] == '0':
                #Trailhead
                waveCoordinates = {(x, y)}
                nextWaveCoordinates = set()
                stepCount = 0
                while len(waveCoordinates) > 0 and stepCount < 9:
                    stepCount += 1
                    for coord in waveCoordinates:
                        #up
                        if (coord[1] - 1 >= 0 and data[coord[1]-1][coord[0]] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0],coord[1]-1))

                        #down
                        if (coord[1] + 1 < len(data) and data[coord[1]+1][coord[0]] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0],coord[1]+1))

                        #left
                        if (coord[0] - 1 >= 0 and data[coord[1]][coord[0]-1] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0]-1,coord[1]))

                        #right
                        if (coord[0] + 1 < len(data[y].rstrip()) and data[coord[1]][coord[0]+1] == str(stepCount)):
                            nextWaveCoordinates.add((coord[0]+1,coord[1]))

                    waveCoordinates = nextWaveCoordinates.copy()
                    nextWaveCoordinates.clear()

                #Add wave coordinate count as this trailhead score
                trailheadsTotalScore += len(waveCoordinates)
    return trailheadsTotalScore

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))