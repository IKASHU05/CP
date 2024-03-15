import math

def solve():
    # If n and then array is given
    n = int(input())
    
    if n==1:
        print("1")
        return    
    count=1
    
    while(count<=n):
        count=count*2
    print(count//2)        



t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1