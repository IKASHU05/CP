import math

def solve():
    # If n and then array is given
    
    k,n,w = [int(x) for x in input().split()]
    cost=0
    bc=k
    for i in range(w):
        bc=k*(i+1)
        cost=cost+bc

    if cost>n:
        borrow=cost-n
        print(borrow)
    else:
        print("0")





t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1































    t = int(input())
for _ in range(t):
  n = int(input())

  a = [int(x) for x in input().split()]
  
  a = sorted(a)

  a[0]= a[0]+1
  prod = 1

  for num in a:
    prod *= num
  

  print(prod)