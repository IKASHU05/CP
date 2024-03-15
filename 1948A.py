def solve():
    # If n and then array is given
    n = int(input())
   
    if n % 2 == 1:
        print("NO")
    else:
        print("YES")
        print("AAB" * (n // 2))

t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1