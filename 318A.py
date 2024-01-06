import math

def solve():
    # If n and then array is given
    
    n,k = [int(x) for x in input().split()]

    
    if n % 2 == 0:
        h = n // 2
    else :
        h = (n // 2) + 1
    if (k<= h):
        print((k * 2) - 1)
    else:
       print((k- h) * 2)
    
    
t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1