import sys
readlines = sys.stdin.readlines
from collections import Counter
from typing import Callable, List, Tuple

inputLines = list(map(lambda s: s.strip(), readlines()))

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

def solvePartOne(inputLines: List[str]) -> None:
    cards, bids = parseInput(inputLines, parseCard)

    cardsAndBids = list(zip(cards, bids))
    cardsAndBids.sort(key=lambda p: getStrength(p[0]))

    totalWinnings = 0
    for rank, cardsAndBid in enumerate(cardsAndBids, start=1):
        _, bid = cardsAndBid
        totalWinnings += bid * rank
    print(totalWinnings)

def parseInput(inputLines: List[str], parseCard: Callable[[str], int]) -> Tuple[List[List[int]], List[int]]:
    cards = []
    bids = []

    for line in inputLines:
        cardsString, bidString = line.split()

        parsedCards = list(parseCard(card) for card in cardsString)
        cards.append(parsedCards)
        bids.append(parseBid(bidString))

    return cards, bids

def parseBid(bidString: str) -> int:
    return int(bidString)

def parseCard(card: str) -> int:
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 11
    if card == "T":
        return 10
    return int(card)

def getStrength(cards: List[int]) -> Tuple[int, List[int]]:
    counts = Counter(cards)
    commons = counts.most_common()

    firstCommonCard, firstCommonCount = commons[0]

    if firstCommonCount == 5:
        return (FIVE_OF_A_KIND, cards)

    if firstCommonCount == 4:
        return (FOUR_OF_A_KIND, cards)

    secondCommonCard, secondCommonCount = commons[1]

    if firstCommonCount == 3 and secondCommonCount == 2:
        return (FULL_HOUSE, cards)

    if firstCommonCount == 3:
        return (THREE_OF_A_KIND, cards)

    if firstCommonCount == 2 and secondCommonCount == 2:
        return (TWO_PAIR, cards)

    if firstCommonCount == 2:
        return (ONE_PAIR, cards)

    return (HIGH_CARD, cards)

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    cards, bids = parseInput(inputLines, parseCard2)

    cardsAndBids = list(zip(cards, bids))
    cardsAndBids.sort(key=lambda p: getStrength2(p[0]))

    totalWinnings = 0
    for rank, cardsAndBid in enumerate(cardsAndBids, start=1):
        _, bid = cardsAndBid
        totalWinnings += bid * rank
    print(totalWinnings)

def parseCard2(card: str) -> int:
    if card == "A":
        return 13
    if card == "K":
        return 12
    if card == "Q":
        return 11
    if card == "J":
        return 1
    if card == "T":
        return 10
    return int(card)

def getStrength2(cards: List[int]) -> Tuple[int, List[int]]:
    counts = Counter(filter(lambda card: card != 1, cards))
    commons = counts.most_common()
    jokerCount = cards.count(1) # joker is 1

    firstCommonCount = commons[0][1] if len(counts) > 0 else 0

    if firstCommonCount + jokerCount == 5:
        return (FIVE_OF_A_KIND, cards)

    if firstCommonCount + jokerCount == 4:
        return (FOUR_OF_A_KIND, cards)

    secondCommonCount = commons[1][1] if len(counts) > 1 else 0

    if firstCommonCount + jokerCount == 3 and secondCommonCount == 2:
        return (FULL_HOUSE, cards)

    if firstCommonCount + jokerCount == 3:
        return (THREE_OF_A_KIND, cards)

    if firstCommonCount + jokerCount == 2 and secondCommonCount == 2:
        return (TWO_PAIR, cards)

    if firstCommonCount + jokerCount == 2:
        return (ONE_PAIR, cards)

    return (HIGH_CARD, cards)

solvePartTwo(inputLines[:])
