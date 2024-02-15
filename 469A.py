import math

def solve():
    # If n and then array is given
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    levels = []
    
    for i in range(1,p[0]+1):
        levels.append(p[i])

    for i in range(1,q[0]+1):
        levels.append(q[i])
    
    levels = set(levels)

    if (len(levels) == n):
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
                


t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1