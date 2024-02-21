import math

def solve():
    # If n and then array is given
    n = int(input())
    arr= [int(x) for x in input().split()]
    add=0
    for i in range(0,2*n,2):
        add+=min(arr[i],arr[i+1])
    print(add)
t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1