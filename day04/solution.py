import re
from pathlib import Path

def solve_part1(data):
    #Return value, occurrence count of "XMAS"
    xmasCount = 0
    xmasRegex = "(?=XMAS|SAMX)"

    #Length of each line, assumption and excludes last char (new line)
    charCount = len(data[0]) - 1
    lineCount = len(data)

    #Construct diagonals
    forwardDiag = [[] for _ in range(charCount + lineCount - 1)]
    backDiag = [[] for _ in range(len(forwardDiag))]
    minBackDiag = -lineCount + 1
    for x in range(charCount):
        for y in range(lineCount):
            forwardDiag[x + y].append(data[y][x])
            backDiag[x-y-minBackDiag].append(data[y][x])
    for diag in forwardDiag:
        xmasCount += len(re.findall(xmasRegex, ''.join(diag)))
    for diag in backDiag:
        xmasCount += len(re.findall(xmasRegex, ''.join(diag)))

    #Check vertical lines
    for i in range(charCount):
        verLine = ''.join([line[i:i+1] for line in data])
        xmasCount += len(re.findall(xmasRegex, verLine))

    #Add count from horizontal lines
    for line in data:
        xmasCount = xmasCount + len(re.findall(xmasRegex, line))

    return xmasCount


def solve_part2(data):
    xmasCount = 0
    charCount = len(data[0]) - 1
    lineCount = len(data)
    for i in range(1, lineCount - 1):
        #Check for X-mas
        for k in range(1, charCount - 1):
            if data[i][k] == 'A':
                #We found an A, assess if its an X-mas
                boundaryCharString = ""
                boundaryCharString += data[i-1][k-1]
                boundaryCharString += data[i-1][k+1]
                boundaryCharString += data[i+1][k+1]
                boundaryCharString += data[i+1][k-1]
                xmasRegex = "MMSS|MSSM|SSMM|SMMS"
                if re.search(xmasRegex, boundaryCharString):
                    xmasCount += 1
    return xmasCount

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))