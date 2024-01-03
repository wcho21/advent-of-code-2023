import sys
readlines = sys.stdin.readlines
from re import search, split
from typing import List, Set, Tuple

inputLines = list(map(lambda s: s.strip(), readlines()))

def solvePartOne(inputLines: List[str]) -> None:
    sumPoints = 0
    for line in inputLines:
        _, winningNumbers, gameNumbers = parseCard(line)

        matchingNumbers = winningNumbers & gameNumbers
        point = getPoint(matchingNumbers)

        sumPoints += point

    print(sumPoints)

def parseCard(line: str) -> Tuple[int, Set[int], Set[int]]:
    CARD_DELIMITER = ": "

    cardIndexLabel, numberFields = line.split(CARD_DELIMITER)
    cardIndex = parseCardIndex(cardIndexLabel)
    winningNumbers, gameNumbers = parseNumberFields(numberFields)

    return cardIndex, winningNumbers, gameNumbers

def getPoint(matchingNumbers: Set[int]) -> int:
    numMatchingNumbers = len(matchingNumbers)

    point = int(2 ** (numMatchingNumbers-1))
    return point

def parseCardIndex(label: str) -> int:
    searched = search(r"[0-9]+", label)
    if searched is None:
        raise Exception(f"invalid label: {label=}")

    index = int(searched.group(0))
    return index

def parseNumberFields(fields: str) -> Tuple[Set[int], Set[int]]:
    """
    parse number lists into sets, and return the sets
    """

    FIELD_DELIMITER = " | "
    NUMBER_DELIMITER = r"\ +"

    winningNumberField, gameNumberField = fields.split(FIELD_DELIMITER)
    winningNumbers = set(map(int, split(NUMBER_DELIMITER, winningNumberField.strip())))
    gameNumbers = set(map(int, split(NUMBER_DELIMITER, gameNumberField.strip())))

    return winningNumbers, gameNumbers

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    scores: List[Tuple[int, int]] = []
    for line in inputLines:
        cardIndex, winningNumbers, gameNumbers = parseCard(line)

        matchingNumbers = winningNumbers & gameNumbers
        score = len(matchingNumbers)

        scores.append((len(matchingNumbers), cardIndex))

    cardCounts = countCards(scores)
    numCards = sum(cardCounts)
    print(numCards)

def countCards(scores: List[Tuple[int, int]]) -> List[int]:
    cardCounts = [0] + [1]*len(scores) # 1-based list; 0 index not used

    for score, cardIndex in scores:
        cardCount = cardCounts[cardIndex]

        copyIndices = range(cardIndex+1, cardIndex+1+score)
        for copyIndex in copyIndices:
            cardCounts[copyIndex] += cardCount

    return cardCounts

solvePartTwo(inputLines[:])
