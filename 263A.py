import math

def solve():
    for i in range(5):
        row = [x for x in input().split()]
       
        for j in range(5):
            if row[j]=='1':
                sum = abs(i - 2) + abs(j-2)
                print(sum)
            
        




t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1