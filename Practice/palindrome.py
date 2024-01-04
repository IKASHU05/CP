def isPalindrome(x: int) -> str:
    # Write your code here  
    ans=0
    rev = ""
    while x!=0:
        digit= x%10
        rev += str(digit)
        x=x//10
        
    return rev

y = int(input())
print(isPalindrome(y))