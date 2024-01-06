import sys
readlines = sys.stdin.readlines
from re import findall
from typing import Callable, List, Tuple

inputLines = list(map(lambda s: s.strip(), readlines()))

def solvePartOne(inputLines: List[str]) -> None:
    times, distances = parseInput(inputLines)

    numWays = 1
    for time, distance in zip(times, distances):
        numWays *= getNumWaysToBeat(time, distance)

    print(numWays)

def parseInput(inputLines: List[str]) -> Tuple[List[int], List[int]]:
    times = readNumbers(inputLines[0])
    distance = readNumbers(inputLines[1])

    return times, distance

def readNumbers(line: str) -> List[int]:
    return list(map(int, findall(r"[0-9]+", line)))

def getNumWaysToBeat(time: int, distance: int) -> int:
    """
    return the number of ways to beat
    """

    # the distance is maximum when the holding time is half of given time
    timeForPeak = time // 2

    leastTimeToBeat = getLeastIndexWhereGreaterThan(distance, 0, timeForPeak, lambda t: getTraveledDistance(time, t))

    # the time value itself is the number of possible outcomes
    # get the number of ways to beat by subtracting the number of ways not to beat from the total
    numWays = (timeForPeak - (leastTimeToBeat-1)) * 2

    # if time is even, there is only one peak, so remove duplicate count
    if time % 2 == 0:
        numWays -= 1

    return numWays

def getTraveledDistance(time: int, holdTime: int) -> int:
    return (time - holdTime) * holdTime

def getLeastIndexWhereGreaterThan(key: int, low: int, high: int, getValueFromIndex: Callable[[int], int]) -> int:
    """
    find the least index where the value is greater then the key
    """

    valAtLow = getValueFromIndex(low)
    valAtHigh = getValueFromIndex(high)

    while low < high:
        mid = low + (high - low) // 2
        valAtMid = getValueFromIndex(mid)

        if valAtMid <= key:
            low = mid + 1
            continue
        high = mid

    return high

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    time, distance = parseInputAsSingleNumber(inputLines)

    print(getNumWaysToBeat(time, distance))

def parseInputAsSingleNumber(inputLines: List[str]) -> Tuple[int, int]:
    time = readNumbersAsSingle(inputLines[0])
    distance = readNumbersAsSingle(inputLines[1])

    return time, distance

def readNumbersAsSingle(line: str) -> int:
    return int("".join(findall(r"[0-9]+", line)))

solvePartTwo(inputLines[:])
