import sys
readlines = sys.stdin.readlines
from re import search
from typing import Callable, List, Tuple

inputLines = list(map(lambda s: s.strip(), readlines()))

MapFunc = Callable[[Tuple[int, str]], Tuple[int, str]]
Interval = Tuple[int, int]

def solvePartOne(inputLines: List[str]) -> None:
    seeds, mapFuncsList = parseInput(inputLines)

    locations = mapSeedsToLocations(seeds, mapFuncsList)

    minLocation = min(locations)
    print(minLocation)

# input parsing functions

def parseInput(lines: List[str]) -> Tuple[List[int], List[List[MapFunc]]]:
    splits = splitLinesBy(inputLines, "")

    seedsLine = splits[0][0]
    mapLinesList = splits[1:]

    seeds = parseSeedsLine(seedsLine)
    mapFuncsList = list(map(parseMapLinesAsFuncs, mapLinesList))

    return seeds, mapFuncsList

def splitLinesBy(lines: List[str], separator: str) -> List[List[str]]:
    splits: List[List[str]] = []

    buffer: List[str] = []
    for line in lines + [separator]:
        if line == separator:
            splits.append(buffer)
            buffer = []
            continue

        buffer.append(line)

    return splits

def parseSeedsLine(line: str) -> List[int]:
    DELIMITER = ": "

    label, seedList = line.split(DELIMITER)

    seeds = list(map(int, seedList.split()))

    return seeds

def parseMapLinesAsFuncs(mapLines: List[str]) -> List[MapFunc]:
    """
    returns list of map functions
    """

    label, *numberLines = mapLines
    sourceCategory, destCategory = parseMapCategories(label)

    numberLists = [list(map(int, line.split())) for line in numberLines]

    mapFuncs: List[MapFunc] = []
    for destBeg, sourceBeg, intervalLen in numberLists:
        mapFunc = createMapFunc(sourceBeg, destBeg, intervalLen, sourceCategory, destCategory)
        mapFuncs.append(mapFunc)

    # identity function for values not within given map intervals
    mapFuncs.append(createCategoryChangingFunc(destCategory))

    return mapFuncs

def parseMapCategories(label: str) -> Tuple[str, str]:
    """
    return source category and destination category
    """

    searched = search(r"([a-z]+)-to-([a-z]+)", label)
    if searched is None:
        raise Exception(f"invalid map label: {label}")

    source, dest = searched.groups()
    return source, dest

def createMapFunc(sourceBeg: int, destBeg: int, intervalLen: int, sourceCategory: str, destCategory: str) -> MapFunc:
    """
    return a closure for a map
    """

    sourceEnd = sourceBeg + intervalLen
    diff = destBeg - sourceBeg

    def mapFunc(toMap: Tuple[int, str]) -> Tuple[int, str]:
        """
        return map function which returns mapped value with destination category,
        if value is within source interval, and category is source category.
        note that interval is half-open, i.e., [beg, end).
        """

        num, category = toMap
        if category != sourceCategory:
            return toMap

        withinInterval = sourceBeg <= num < sourceEnd
        if not withinInterval:
            return toMap

        return (num + diff, destCategory)

    return mapFunc

def createCategoryChangingFunc(destCategory: str) -> MapFunc:
    """
    return identity function, just changing category
    """

    def mapFunc(toMap: Tuple[int, str]) -> Tuple[int, str]:
        num, _ = toMap
        return (num, destCategory)

    return mapFunc

# map logic functions

def mapSeedsToLocations(seeds: List[int], mapFuncsList: List[List[MapFunc]]) -> List[int]:
    # attach category to values
    seedsToMap = list(zip(seeds, ["seed"] * len(seeds)))

    mappedLocation = list(map(lambda seed: mapSeedToLocation(seed, mapFuncsList), seedsToMap))

    # remove category from values
    locations = list(map(lambda pair: pair[0], mappedLocation))

    return locations

def mapSeedToLocation(seed: Tuple[int, str], mapFuncsList: List[List[MapFunc]]) -> Tuple[int, str]:
    """
    return location value, mapped by map functions for each category
    """

    toMap = seed

    for mapFuncs in mapFuncsList:
        toMap = mapToNextCategory(toMap, mapFuncs)
    mapped = toMap

    return mapped

def mapToNextCategory(value: Tuple[int, str], mapFuncs: List[MapFunc]) -> Tuple[int, str]:
    """
    return value, mapped by map functions for a category
    """

    toMap = value

    for mapFunc in mapFuncs:
        toMap = mapFunc(toMap)
    mapped = toMap

    return mapped

solvePartOne(inputLines[:])

def solvePartTwo(inputLines: List[str]) -> None:
    seedIntervals, mapIntervalsList, mapFuncsList = parseInputAsIntervals(inputLines)

    mappedIntervals = mapSeedIntervalsToLocationIntervals(seedIntervals, mapIntervalsList, mapFuncsList)

    intervalBegs = list(map(lambda interval: interval[0], mappedIntervals))
    minBeg = min(intervalBegs)
    print(minBeg)

# input parsing functions

def parseInputAsIntervals(lines: List[str]):
    splits = splitLinesBy(inputLines, "")

    seedsLine = splits[0][0]
    mapLinesList = splits[1:]

    seedIntervals = parseSeedsLineAsIntervals(seedsLine)
    mapIntervalsList = list(map(parseMapLinesAsIntervals, mapLinesList))
    mapFuncsList = list(map(parseMapLinesAsFuncs, mapLinesList))
    return seedIntervals, mapIntervalsList, mapFuncsList

def parseMapLinesAsIntervals(lines: List[str]):
    numLinesList = lines[1:]

    intervals: List[Interval] = []
    for numLines in numLinesList:
        _, beg, length = map(int, numLines.split())
        end = beg+length

        intervals.append((beg, end))

    return intervals

def parseSeedsLineAsIntervals(line: str) -> List[Interval]:
    label, numsField = line.split(": ")

    nums = list(map(int, numsField.split()))

    intervals: List[Interval] = []
    for i in range(0, len(nums), 2):
        beg = nums[i]
        length = nums[i+1]
        end = beg+length

        intervals.append((beg, end))

    return intervals

# map logic functions

def mapSeedIntervalsToLocationIntervals(seedIntervals: List[Interval], mapIntervalsList: List[List[Interval]], mapFuncsList: List[List[MapFunc]]) -> List[Interval]:
    categories = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]

    intervalsToMap = seedIntervals

    for mapIntervals, mapFuncs, sourceCategory in zip(mapIntervalsList, mapFuncsList, categories):
        intervalsToMap = splitIntervalsByIntervals(intervalsToMap, mapIntervals)

        mapped = mapIntervalsToNextCategory(intervalsToMap, mapFuncs, sourceCategory)
        intervalsToMap = mapped

    mapped = intervalsToMap

    return mapped


def mapIntervalsToNextCategory(intervals: List[Interval], mapFuncs: List[MapFunc], sourceCategory: str) -> List[Interval]:
    mapped: List[Interval] = []
    for beg, end in intervals:
        toMapBeg = (beg, sourceCategory)
        toMapEnd = (end-1, sourceCategory) # -1 due to open interval

        # drop category (second element) and take value only
        mappedBeg = mapToNextCategory(toMapBeg, mapFuncs)[0]
        mappedEnd = mapToNextCategory(toMapEnd, mapFuncs)[0] + 1 # +1 to restore open interval

        mapped.append((mappedBeg, mappedEnd))

    return mapped

# interval split functions

def splitIntervalsByIntervals(toSplits: List[Interval], splitters: List[Interval]) -> List[Interval]:
    splits: List[Interval] = []

    for toSplit in toSplits:
        splits += splitIntervalByIntervals(toSplit, splitters)

    return splits

def splitIntervalByIntervals(toSplit: Interval, splitters: List[Interval]) -> List[Interval]:
    targets = [toSplit]

    for splitter in splitters:
        result: List[Interval] = []

        for target in targets:
            result += splitIntervalByInterval(target, splitter)

        targets = result

    return targets

def splitIntervalByInterval(toSplit: Interval, splitter: Interval) -> List[Interval]:
    toSplitBeg, toSplitEnd = toSplit
    splitterBeg, splitterEnd = splitter

    splits: List[Interval] = []

    if toSplitBeg < splitterBeg < toSplitEnd:
        splits.append((toSplitBeg, splitterBeg))
        toSplitBeg = splitterBeg

    if toSplitBeg < splitterEnd < toSplitEnd:
        splits.append((toSplitBeg, splitterEnd))
        toSplitBeg = splitterEnd

    splits.append((toSplitBeg, toSplitEnd))

    return splits

solvePartTwo(inputLines[:])
