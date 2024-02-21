import math

def solve():
    
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    triangle = False
       
    for i in range(n):
        for j in range(1,n-1):
            if grid[i][j]=="1":
                if (grid[i][j-1] == "0" and grid[i][j+1] == "0"):
                    triangle = True
                    break
    
    if triangle:
        print("TRIANGLE")
    else:
        print("SQUARE")
t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1