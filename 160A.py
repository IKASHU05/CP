import math

def solve():
    # If n and then array is given
    n = int(input())
    value = [int(x) for x in input().split()]
    value.sort()
    total=sum(value)
    
t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1