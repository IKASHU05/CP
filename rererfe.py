import math

def solve():
    # If n and then array is given
    n = int(input())
    arr = [int(x) for x in input().split()]
    for i in  range(n):
        sum+=abs(arr[i])
     
    print((sum))

t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1