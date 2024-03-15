def solve():
    # If n and then array is given
    n,p = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr = sorted(arr)
    money=0   
     
    for i in range(p):

        if arr[i]<0:
            money+=arr[i]
            
                

    print(abs(money))        
            

    

t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1