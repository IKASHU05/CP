import math

def solve():
    n = int(input())

    ans = n & (n-1)    

    
    print("YES") if ans == 0 else print("NO")
    
       
    
    # 0 0 0 0 0 1 0 0 0 0 0 0 0 0
    # 0 0 0 0 0 0 1 1 1 1 1 1 1 1
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0


    # 0 0 0 0 0 0 0 0 0 1 1 0 0 0
    # 0 0 0 0 0 0 0 0 0 0 1 1 1 1

   



t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1