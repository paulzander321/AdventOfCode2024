from pathlib import Path

#Basic fault checks
#Runs in O(n) time, requires O(n) space
def safeReport(report):
    reportIncreasing = False
    i = 0
    n = len(report)
    while i < n:
        #Initialize the order of levels
        if i == 1:
            if report[i] - report[i - 1] > 0:
                reportIncreasing = True
        if i > 0:
            #Duplicant check
            if abs(report[i] - report[i - 1]) == 0:
                return False
            #Distance check
            if abs(report[i] - report[i - 1]) > 3:
                return False
            #Ordering check
            if reportIncreasing and report[i] - report[i - 1] < 0:
                return False
            elif not reportIncreasing and report[i] - report[i - 1] > 0:
                return False
        i+=1  
    return True


#Unfinished, requires some weird manipulations
def safeReportWithFaultTolerance(report):
    faultFound = False
    reportIncreasing = False
    i = 0
    n = len(report)
    while i < n:
        #initialize flag for increasing vs decreasing levels
        if i == 1:
            if report[i] - report[i - 1] > 0:
                reportIncreasing = True

        if i > 0:
            #check if values are the same (duplicates)
            if abs(report[i] - report[i - 1]) == 0:
                if not faultFound:
                    report.pop(i)
                    n-=1
                    faultFound = True
                    continue
                else:
                    return False
            
            #check if values differ by more than 3
            if abs(report[i] - report[i - 1]) > 3:
                if not faultFound:
                    if i == n-1:
                        #Prune the end
                        report.pop(i)
                        n-=1
                        faultFound = True
                        continue
                    else:
                        #Trickier, need to determine if we can safely remove a level
                        if abs(report[i-1] - report[i+1]) <= 3:
                            report.pop(i)
                            n-=1
                            faultFound = True
                            continue
                        elif i == 1:
                            report.pop(i-1)
                            n-=1
                            faultFound = True
                        else:
                            return False
                else:
                    return False

            #ensure report continues to increase
            if reportIncreasing and report[i] - report[i - 1] < 0:
                return False

            #ensure report continues to decrease
            if not reportIncreasing and report[i] - report[i - 1] > 0:
                return False
        i+=1
    return True


#Uses recursion, it has high space and time complexity :/
def safeReportRecursive(report, faultDetected):
    reportIncreasing = False
    i = 0
    n = len(report)

    while i < n:
        if i == 1:
            if report[i] - report[i - 1] > 0:
                reportIncreasing = True

        if i > 0:
            #Check if there are adjacent duplicates
            if abs(report[i] - report[i - 1]) == 0:
                if faultDetected:
                    return False
                else:
                    prunedReport = list(report)
                    prunedReport.pop(i)
                    return safeReportRecursive(prunedReport, True)
            
            #Check for difference more than 3 for adjacent levels
            if abs(report[i] - report[i - 1]) > 3:
                if faultDetected:
                    return False
                else:
                    prunedReportRemoveCur = list(report)
                    prunedReportRemoveCur.pop(i)
                    prunedReportRemovePrev = list(report)
                    prunedReportRemovePrev.pop(i-1)
                    if safeReportRecursive(prunedReportRemoveCur, True):
                        return True
                    else:
                        return safeReportRecursive(prunedReportRemovePrev, True)                    
            
            if reportIncreasing and report[i] - report[i - 1] < 0:
                if faultDetected:
                    return False
                else:
                    prunedReportRemoveCur = list(report)
                    prunedReportRemoveCur.pop(i)
                    if safeReportRecursive(prunedReportRemoveCur, True):
                        return True
                    else:
                        prunedReportRemovePrev = list(report)
                        prunedReportRemovePrev.pop(i-1)
                        return safeReportRecursive(prunedReportRemovePrev, True)
            
            if not reportIncreasing and report[i] - report[i - 1] > 0:
                if faultDetected:
                    return False
                else:
                    prunedReportRemoveCur = list(report)
                    prunedReportRemoveCur.pop(i)
                    if safeReportRecursive(prunedReportRemoveCur, True):
                        return True
                    else:
                        prunedReportRemovePrev = list(report)
                        prunedReportRemovePrev.pop(i-1)
                        if safeReportRecursive(prunedReportRemovePrev, True):
                            return True
                        elif i == 2:
                            prunedReportRemoveFirst = list(report)
                            prunedReportRemoveFirst.pop(0)
                            return safeReportRecursive(prunedReportRemoveFirst, True)

        i+=1
            
    return True


#This is really bad, brute force way to do it
def safeReportBad(report):
    if safeReport(report):
        return True
    for i in range(len(report)):
        prunedReport = list(report)
        prunedReport.pop(i)
        if safeReport(prunedReport):
            return True
    return False


def solve_part1(data):
    safeReportCount = 0
    reports = []
    for line in data:
        reports.append(list(map(int, line.split())))

    for report in reports:
        safeReportCount += safeReport(report)
            
    return safeReportCount


def solve_part2(data, recursive = False, methodical = False):
    safeReportCount = 0
    reports = []
    for line in data:
        reports.append(list(map(int, line.split())))

    if recursive:
        script_dir = Path(__file__).parent
        with open(script_dir / "outputRecursive.txt", "w") as file:
            pass
    elif methodical:
        script_dir = Path(__file__).parent
        with open(script_dir / "outputMethodical.txt", "w") as file:
            pass
    else:
        script_dir = Path(__file__).parent
        with open(script_dir / "outputBad.txt", "w") as file:
            pass

    for report in reports:
        if recursive:
            if safeReportRecursive(report, False):
                script_dir = Path(__file__).parent
                with open(script_dir / "outputRecursive.txt", "a") as file:
                    file.write(f"{report}\n")
                safeReportCount += 1
        elif methodical:
            if safeReportWithFaultTolerance(report):
                script_dir = Path(__file__).parent
                with open(script_dir / "outputMethodical.txt", "a") as file:
                    file.write(f"{report}\n")
                safeReportCount += 1
        else:
            if safeReportBad(report):
                script_dir = Path(__file__).parent
                with open(script_dir / "outputBad.txt", "a") as file:
                    file.write(f"{report}\n")
                safeReportCount += 1
            
    return safeReportCount


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))
    print("Part 2 (recursive):", solve_part2(raw_data, recursive=True))
    print("Part 2 (methodical):", solve_part2(raw_data, methodical=True))