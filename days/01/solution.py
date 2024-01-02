import sys
readlines = sys.stdin.readlines
from re import findall, sub
from typing import List

inputLines = list(map(lambda s: s.strip(), readlines()))

def solvePartOne(inputLines: List[str]) -> None:
    allDigits = list(map(readDigits, inputLines))
    sumCalibrations = sum(map(readFirstAndLast, allDigits))

    print(sumCalibrations)

def readDigits(s: str) -> List[str]:
    return findall(r"[0-9]", s)

def readFirstAndLast(s: List[str]) -> int:
    return int(s[0] + s[-1])

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    replaced = list(map(replaceLetters, inputLines))

    allDigits = list(map(readDigits, replaced))
    sumCalibrations = sum(map(readFirstAndLast, allDigits))

    print(sumCalibrations)

def replaceLetters(line: str) -> str:
    LETTERS_LIST = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    REPLACED_LIST = ["o1e", "t2o", "t3e", "4", "5e", "6", "7n", "e8t", "n9e"]

    for letters, replaced in zip(LETTERS_LIST, REPLACED_LIST):
        line = sub(letters, replaced, line)
    return line

solvePartTwo(inputLines[:])
