import math

def solve():
    # If n and then array is given
    n = int(input())
    path = input()

    coins = 0
    for i in range(n-1):
        if path[i] == "@":
            coins += 1
        if i==n-2 and path[n-1] == "@":
            coins+=1
        elif path[i] == "*" and path[i+1] == "*":
            break
    
    print(coins)
    
 
t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1