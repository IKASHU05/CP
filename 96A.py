import math

def solve():
    # If n and then array is given
    
    team =input()
    count=0
    num=False
    coun=0
    for i in range(len(team)):
        if team[i]=='1':
            count +=1
            coun=0
        if team[i]=='0':
            coun +=1
            count=0
        if count>=7 or coun>=7:
            num=True
            break
    if num==True:
        print("YES")
    else:
        print("NO")        


t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1