def solve():
    # If n and then array is given
    # n = int(input())
    n,m = [int(x) for x in input().split()]
    days = 1
    while(n>0): 
        if (days%m==0): n += 1
        n -= 1
        days += 1
    print(days-1)
     
    
t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1