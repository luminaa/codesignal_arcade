def solution(inputArray):
    max_length = max(len(s) for s in inputArray)
    return [s for s in inputArray if len(s) == max_length]