import math

def solve():
    # If n and then array is given
    n = int(input())
    v= [int(x) for x in input().split()]
    value=0
    coins=0
    cv=0
    for i in range(len(v)):
        value= value + v[i]
    v.sort(reverse=True)
    i=0
    while(cv<=value//2):
        
        cv=cv+v[i]
        i+=1
        coins+=1  
          
        
        
    print(coins)

t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1