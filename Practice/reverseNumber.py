def reverseNumber(x: int) -> int:
    # Write your code here
    
    ans=0
    while x!=0:
        digit= x%10
        ans=ans*10+digit
        x=x//10
    return(ans)


y = int(input())
print(reverseNumber(y))