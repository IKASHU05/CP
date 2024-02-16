import math

def solve():
    # If n and then array is given
    a,b = [int(x) for x in input().split()]
    count=0
    while(a<=b):
        a=a*3
        b=b*2
        count+=1
    print(count)

t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1