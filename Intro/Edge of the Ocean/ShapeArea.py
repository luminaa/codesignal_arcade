# fast solution
def solution(n):
    return n**2 + (n-1)**2

# recursive solution
def solution(n):
    if n == 1:
        return 1
    else: 
        return solution(n-1) + 4*(n-1)