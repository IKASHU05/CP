import math

def solve():
    # If n and then array is given
    
    a,b = [int(x) for x in input().split()]
    
      
    if (a + b) % 2 == 0:
        print("Bob")
    else:
        print("Alice")
t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1