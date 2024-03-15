def solve():
    # If n and then array is given
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    MAX = 2*(arr[-1] - arr[0]) + (arr[-2] - arr[1])

    print(MAX) 
    
    
t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1