

def solve():
    # If n and then array is given
    n = int(input())
    arr = [int(x) for x in input().split()]
    count=0
    for i in range(n):
        s = abs(arr[i])
        count+=s
    print(count)

t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1