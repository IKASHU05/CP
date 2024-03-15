import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def solve():
    # If n and then array is given
    s=input()

    m = int(input())
    
    count=0
    pre = []

    pre.append(0)

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        pre.append(count)
    
    pre.append(count)


    for i in range(m):
        l,r = [int(x) for x in input().split()]

        ans = pre[r-1] - pre[l-1]   

        print(ans)



solve()