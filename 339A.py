import math

def solve():
    # If n and then array is given
    s = input()
    c1=0
    c2=0
    c3=0
    count=""
    for i in range(len(s)):
        if s[i] == '1':
            c1+=1
            i+=1
        elif s[i] == '2':
            c2+=1
            i+=1
        elif s[i] =='3':
            c3+=1
            i+=1
        else :
            i+=1
    for i in range(c1):
        count+='1+'
    for i in range(c2):
        count+='2+'
    for i in range(c3):
        count+='3+' 
    
    print(count[:-1])       
        
            



t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1