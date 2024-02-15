import math

def solve():
    # If n and then array is given
    n = input()
    l=0
    u=0
    for i in n:
        
        if ord(i)>=65 and  ord(i)<=90:
            u+=1
        if ord(i)>=97 and ord(i)<=122:    
            l+=1
    if l>=u:
        n=n.lower()
        print(n)
    else :
        n=n.upper()
        print(n)

t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1

