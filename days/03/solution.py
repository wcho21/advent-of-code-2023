import sys
readlines = sys.stdin.readlines
from collections import defaultdict
from itertools import chain
from typing import Dict, List, Tuple

class NumberToken:
    def __init__(self, value, begX, endX):
        self.value = value
        self.begX = begX
        self.endX = endX

    def __hash__(self):
        return hash((self.value, self.begX, self.endX))

    def __eq__(self, other):
        return self.value == other.value and self.begX == other.begX and self.endX == other.endX

    def __repr__(self):
        return f'(NumberToken: {self.value=}, {self.begX=}, {self.endX=})'

class SymbolToken:
    def __init__(self, value, x):
        self.value = value
        self.x = x

    def __hash__(self):
        return hash((self.value, self.x))

    def __eq__(self, other):
        return self.value == other.value and self.x == other.x

    def __repr__(self):
        return f'(SymbolToken: {self.value=}, {self.x=})'

inputLines = list(map(lambda s: s.strip(), readlines()))

def solvePartOne(inputLines: List[str]) -> None:
    numbers, symbols = parseSchematic(inputLines)
    adjacentNumbers = getAdjacentNumbers(numbers, symbols)
    print(addUpAdjacentNumbers(adjacentNumbers))

def parseSchematic(lines: List[str]) -> Tuple[List[List[NumberToken]], List[List[SymbolToken]]]:
    """
    returns number tokens and symbol tokens for each line
    """

    numbers = parseSchematicNumbers(lines)
    symbols = parseSchematicSymbols(lines)

    return numbers, symbols

def getAdjacentNumbers(numberTokens: List[List[NumberToken]], symbolTokens: List[List[SymbolToken]]) -> Dict[SymbolToken, List[int]]:
    """
    returns adjacent numbers for each symbol, for each line
    """

    adjacentNumbers: Dict[SymbolToken, List[int]] = defaultdict(list)

    for symbolY in range(len(symbolTokens)):
        for dy in (-1, 0, 1):
            numberY = symbolY + dy

            if numberY < 0 or numberY >= len(numberTokens):
                continue

            adjacentNumbersForLine = getAdjacentNumbersForLine(numberTokens[numberY], symbolTokens[symbolY])
            for symbol, numbers in adjacentNumbersForLine.items():
                for number in numbers:
                    adjacentNumbers[symbol].append(number)

    return adjacentNumbers

def addUpAdjacentNumbers(adjacentNumbers: Dict[SymbolToken, List[int]]) -> int:
    return sum(sum(numbers) for numbers in adjacentNumbers.values())

def getAdjacentNumbersForLine(numbers: List[NumberToken], symbols: List[SymbolToken]) -> Dict[SymbolToken, List[int]]:
    """
    returns adjacent numbers for each symbol, using two-pointer technique
    """

    numberPointer = 0
    symbolPointer = 0

    adjacentNumbers: Dict[SymbolToken, List[int]] = defaultdict(list)

    while numberPointer < len(numbers) and symbolPointer < len(symbols):
        number = numbers[numberPointer]
        symbol = symbols[symbolPointer]

        if number.endX < symbol.x-1: # number is not adjacent and before symbol
            numberPointer += 1
            continue
        if number.begX > symbol.x+1: # number is not adjacent and after symbol
            symbolPointer += 1
            continue

        adjacentNumbers[symbol].append(number.value)

        # if number is at the left of symbol, move to next number
        # since adjacent number can be at the right of symbol
        if number.endX == symbol.x-1:
            numberPointer += 1
            continue

        numberPointer += 1
        symbolPointer += 1

    return adjacentNumbers

def parseSchematicNumbers(lines: List[str]) -> List[List[NumberToken]]:
    tokens = [parseSchematicNumbersForLine(line) for line in lines]

    return tokens

def parseSchematicSymbols(lines: List[str]) -> List[List[SymbolToken]]:
    tokens = [parseSchematicSymbolsForLine(line) for line in lines]

    return tokens

def parseSchematicNumbersForLine(line: str) -> List[NumberToken]:
    SENTINEL_DIGIT = ('.', -1)

    digits = [(char, x) for x, char in enumerate(line) if char.isdigit()]
    digitsShifted = digits[1:] + [SENTINEL_DIGIT]

    tokens = []
    buffer = []
    for (curDigit, curX), (nextDigit, nextX) in zip(digits, digitsShifted):
        buffer.append((curDigit, curX))

        if curX == nextX-1:
            continue

        tokens.append(parseIntoNumberToken(buffer))

        buffer = []

    return tokens

def parseSchematicSymbolsForLine(line: str) -> List[SymbolToken]:
    isSymbol = lambda char: not char.isdigit() and char != "."

    tokens = [SymbolToken(char, x) for x, char in enumerate(line) if isSymbol(char)]

    return tokens

def parseIntoNumberToken(digitsAndXs: List[Tuple[str, int]]) -> NumberToken:
    digits, xs = list(zip(*digitsAndXs))

    number = int("".join(digits))
    begX, endX = xs[0], xs[-1]

    return NumberToken(number, begX, endX)

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    numbers, symbols = parseSchematic(inputLines)
    gearSymbols = filterOutExceptGears(symbols)
    adjacentNumbers = getAdjacentNumbers(numbers, gearSymbols)
    print(addUpGearRatios(adjacentNumbers))

def filterOutExceptGears(symbols: List[List[SymbolToken]]) -> List[List[SymbolToken]]:
    filtered = []
    for symbolsForLine in symbols:
        filteredLine = [symbol for symbol in symbolsForLine if symbol.value == "*"]
        filtered.append(filteredLine)

    return filtered

def addUpGearRatios(adjacentNumbers: Dict[SymbolToken, List[int]]) -> int:
    total = 0
    for numbers in adjacentNumbers.values():
        if len(numbers) != 2:
            continue

        total += numbers[0] * numbers[1]

    return total

solvePartTwo(inputLines[:])
