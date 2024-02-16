

def solve():
    # If n and then array is given
    n = int(input())
    if n%5==0:
        print(n//5)
    else:
        print(n//5+1)
   
t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1