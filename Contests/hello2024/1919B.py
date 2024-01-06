import math

def solve():
    # If n and then array is given
    n = int(input())
    arr = input()
    count=0
    for i in arr:
        if i=='+':
            count+=1
        elif i=='-':
            count-=1
            
    print(abs(count))            
            
                
            

            




t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1



 