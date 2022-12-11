def solution(statues):
    maxi = max(statues)
    mini = min(statues)
    n = len(statues)
    return maxi + 1 - mini - n