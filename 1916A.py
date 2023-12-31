import math

def solve():
    # If n and then array is given
    n,k = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    sum = 1
    for i in b:
        sum = sum * i


    if 2023 % sum  != 0:
        print("NO", end=" ")
    elif 2023 % sum  == 0:
        print("YES")
        print(2023//sum, end=" ")
        for i in range(k-1):
            print("1",end=" ")
    
    print()

    
    



t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1