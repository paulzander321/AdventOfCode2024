import math
from z3 import *
from pathlib import Path

class PageRule:
    def __init__(self, beforePage, afterPage):
        self.beforePage = beforePage
        self.afterPage = afterPage

    def ruleMet(self, update):
        pages = update.split(",")
        if self.beforePage in pages and self.afterPage in pages:
            return pages.index(self.beforePage) < pages.index(self.afterPage)
        else:
            return True
    
    def ruleApplicable(self, update):
        return self.beforePage in update and self.afterPage in update
        
class PageRuleBook:
    def __init__(self):
        self.rules = []

    def addRule(self, rule):
        self.rules.append(rule)

    def verifyAndFixUpdate(self, update):
        pages = update.split(",")

        #Using solver, this is not a good scenario for using an SMT solver but
        #it doubles as syntax practice for my upcoming declarative final :)
        s = Solver()

        #Create the variables for Z3 SMT (satisfiability modulo theory solver)
        pageVars = {page: Int(page) for page in pages}
        for page in pages:
            s.add(pageVars[page] > 0)

        #Add constraints based on the page rules
        for rule in self.rules:
            if rule.ruleApplicable(update):
                s.add(pageVars[rule.beforePage] < pageVars[rule.afterPage])

        #Check the solver returned a valid model, use to sort pages
        if s.check() == sat:
            model = s.model()
            sorted_pages = sorted(pages, key=lambda p: model[pageVars[p]].as_long())
            return sorted_pages
        else:
            return pages


def solve_part1(data):
    correctPageMiddleCount = 0
    pageRules = []
    updates = []
    for line in data:
        if "|" in line:
            pageRules.append(PageRule(line.rstrip('\n').split("|")[0], line.rstrip('\n').split("|")[1]))
        elif "," in line:
            updates.append(line.rstrip('\n'))
    for update in updates:
        updateValid = True
        for rule in pageRules:
            if not rule.ruleMet(update):
                updateValid = False
                break
        if updateValid:
            pages = update.split(",")
            middlePageIndex = math.floor(len(pages) / 2)
            correctPageMiddleCount += int(pages[middlePageIndex])
    return correctPageMiddleCount


def solve_part2(data):
    correctPageMiddleCount = 0
    pageRuleBook = PageRuleBook()
    updates = []
    for line in data:
        if "|" in line:
            pageRuleBook.addRule(PageRule(line.rstrip('\n').split("|")[0], line.rstrip('\n').split("|")[1]))
        elif "," in line:
            updates.append(line.rstrip('\n'))
    for update in updates:
        updateValid = True
        for rule in pageRuleBook.rules:
            if not rule.ruleMet(update):
                updateValid = False
                break
        if not updateValid:
            updatedUpdate = pageRuleBook.verifyAndFixUpdate(update)
            middlePageIndex = math.floor(len(updatedUpdate) / 2)
            correctPageMiddleCount += int(updatedUpdate[middlePageIndex])
    return correctPageMiddleCount


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "input.txt"

    with open(input_file, 'r') as file:
        raw_data = file.readlines()

    print("Part 1:", solve_part1(raw_data))
    print("Part 2:", solve_part2(raw_data))