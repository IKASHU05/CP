import math

def solve():
    # If n and then array is given
    n = int(input())
    curr = ""
    for i in range(1,n+1):
        
        # If i is even
        if (i%2)==0:
            curr += "I love "
        
        # If i is odd
        else:
            curr += "I hate "

        # If i is last
        if (i==n):
            curr += "it"

        # If i is not last
        else:
            curr += "that "

    print(curr)
        




t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1