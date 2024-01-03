import math

def solve():
    
    s = input()
    t = input()
    if (len(s) != len(t)):
        print("NO")
        return
    for i in range(len(s)):
        if s[i]!=t[len(s)-(i+1)]:
           print("NO")
           return
    print("YES")

    j



t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1