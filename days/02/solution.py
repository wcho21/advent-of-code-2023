import sys
readlines = sys.stdin.readlines
from collections import defaultdict
from functools import reduce
from operator import mul
from re import search
from typing import Dict, List, Tuple

inputLines = list(map(lambda s: s.strip(), readlines()))

def solvePartOne(inputLines: List[str]) -> None:
    parsed = list(map(parseLine, inputLines))
    possibleIds = sum(map(getGameIdIfPossibleGame, parsed))

    print(possibleIds)

def getGameIdIfPossibleGame(game: Tuple[int, List[Dict[str, int]]]) -> int:
    gameId, cubeSets = game

    possible = all(map(isPossibleCubeSet, cubeSets))

    return gameId if possible else 0

def parseLine(line: str) -> Tuple[int, List[Dict[str, int]]]:
    """
    returns game id, cube sets
    """

    GAME_ID_DELIMITER = ": "

    gameIdLabel, cubeList = line.split(GAME_ID_DELIMITER)
    gameId = parseGameIdLabel(gameIdLabel)
    cubeSets = parseCubeList(cubeList)

    return gameId, cubeSets

def parseGameIdLabel(label: str) -> int:
    searched = search(r"[0-9]+", label)
    if searched is None:
        raise Exception(f'invalid label: {label=}')

    return int(searched.group(0))

def parseCubeList(cubeList: str) -> List[Dict[str, int]]:
    ENTRY_DELIMITER = "; "

    entries = cubeList.split(ENTRY_DELIMITER)
    cubeSets = list(map(parseCubeListEntry, entries))
    return cubeSets

def parseCubeListEntry(entry: str) -> Dict[str, int]:
    """
    returns {color: amount}
    """

    SUBSET_DELIMITER = ", "

    counts: Dict[str, int] = dict()

    cubes = entry.split(SUBSET_DELIMITER)
    for cube in cubes:
        amountStr, color = cube.split(" ")
        amount = int(amountStr)

        counts[color] = amount

    return counts

def isPossibleCubeSet(cubeSet: Dict[str, int]) -> bool:
    if "red" in cubeSet and cubeSet["red"] > 12:
        return False
    if "green" in cubeSet and cubeSet["green"] > 13:
        return False
    if "blue" in cubeSet and cubeSet["blue"] > 14:
        return False
    return True

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    parsed = list(map(parseLine, inputLines))

    sumPower = 0
    for game in parsed:
        _, cubeSets = game

        amounts = getMaxCubeAmounts(cubeSets)
        power = reduce(mul, amounts.values(), 1)

        sumPower += power

    print(sumPower)

def getMaxCubeAmounts(cubeSets: List[Dict[str, int]]) -> Dict[str, int]:
    """
    returns {color: max amount}
    """

    maxes = {"red": 0, "green": 0, "blue": 0}

    for cubeSet in cubeSets:
        for color, amount in cubeSet.items():
            maxes[color] = max(maxes[color], amount)

    return maxes

solvePartTwo(inputLines[:])
