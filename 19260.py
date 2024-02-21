import math

def solve():
    # If n and then array is given
    # n = int(input())
    s = input().strip()
   
    counta = s.count('A')
    countb = s.count('B')
    if counta > countb:
        print('A')
    else:
        
        print("B")
  

t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1