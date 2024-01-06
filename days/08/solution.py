import sys
readlines = sys.stdin.readlines
from math import lcm
from typing import Tuple, Dict, List

inputLines = list(map(lambda s: s.strip(), readlines()))

def solvePartOne(inputLines: List[str]) -> None:
    instructions, nodes = parseInput(inputLines)

    numSteps = countSteps(instructions, nodes)
    print(numSteps)

def parseInput(lines: List[str]):
    instructions = lines[0]

    nodes: Dict[str, Tuple[str, str]] = dict()

    for line in lines[2:]:
        # use index to parse since the input has a fixed-width format
        label = line[:3]
        left = line[7:10]
        right = line[12:15]

        nodes[label] = (left, right)

    return instructions, nodes

def countSteps(instructions: str, nodes: Dict[str, Tuple[str, str]]) -> int:
    steps = 0
    label = "AAA"

    while label != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        steps += 1

        label = getNextLabel(nodes, label, instruction)

    return steps

def getNextLabel(nodes: Dict[str, Tuple[str, str]], label: str, instruction: str) -> str:
    node = nodes[label]

    if instruction == "L":
        return node[0]
    if instruction == "R":
        return node[1]

    raise Exception(f"bad instruction '{instruction}'")

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    instructions, nodes = parseInput(inputLines)
    startLabels = getStartLabelsFromInput(inputLines)

    numSteps = countSteps2(instructions, nodes, startLabels)
    print(numSteps)

def countSteps2(instructions: str, nodes: Dict[str, Tuple[str, str]], startLabels: List[str]) -> int:
    numStartLabels = len(startLabels)

    current = startLabels
    stepsForEndLabel: Dict[str, int] = dict()
    steps = 0
    while True:
        if len(stepsForEndLabel) == numStartLabels: # all end label encountered
            break

        instruction = instructions[steps % len(instructions)]
        steps += 1

        nextLabels: List[str] = []
        for label in current:
            nextLabel = getNextLabel(nodes, label, instruction)
            nextLabels.append(nextLabel)

            if isEndLabel(nextLabel) and nextLabel not in stepsForEndLabel:
                stepsForEndLabel[nextLabel] = steps

        current = nextLabels

    stepsForEnd = lcm(*stepsForEndLabel.values())
    return stepsForEnd

def getStartLabelsFromInput(lines: List[str]):
    startLabels: List[str] = []

    for line in lines[2:]:
        label = line[:3]

        if isStartLabel(label):
            startLabels.append(label)

    return startLabels

def isStartLabel(label: str) -> bool:
    return label[2] == "A"

def isEndLabel(label: str) -> bool:
    return label[2] == "Z"

solvePartTwo(inputLines[:])
