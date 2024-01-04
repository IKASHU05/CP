import math

def solve():
    # If n and then array is given
    
    a,b,c = [int(x) for x in input().split()]
    if a+b==c:
        print("+")
    else:
        print("-")    


t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1