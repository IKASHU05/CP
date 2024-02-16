import math

def solve():
    # If n and then array is given
    n = int(input())
    if n%2==1:
        print(0)
        return
    elif n%4==0:
        print(n//4-1)
        return
    elif n%4!=0:
        print(n//4)
        return
        
t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1