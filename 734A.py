def solve():
    # If n and then array is given
    n = int(input())
    arr = input()
    ANTON=0
    DANIK=0
    for i in range(n):
        if arr[i]=='A':
            ANTON+=1
        else :
            DANIK+=1
    if ANTON<DANIK:
        print("Danik")
    elif ANTON==DANIK:
        print("Friendship")
    else:
        print("Anton")    
t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1