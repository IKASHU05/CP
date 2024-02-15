

def solve():
    # If n and then array is given
    n=int(input())
    a=input()
    b=input()
    c=input()
    

    for i in range(n):
        if a[i] == b[i]:
            if c[i] != a[i]:
                return False
        else:
            
            if c[i] == a[i] or c[i] == b[i]:
                return True
    return False
def ish():
 if solve():
     print("NO")
 else:
    print("YES")


t = 1
t = int(input())

while t > 0:
    ish()
    t -= 1
