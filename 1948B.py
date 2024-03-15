def sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
def sort(arr):
    for i in range(len(arr) - 1):
        if arr[i]>arr[i+1]:
            if arr[i] >= 10:
                digits = [int(d) for d in str(arr[i])]
                arr.pop(i)
                arr[i:i]=digits
                return sort(arr)
    return sorted(arr)    
    
t = 1
t = int(input())

while t > 0:
    n = int(input())
    arr= list(map(int, input().split()))
    if sort(arr):
        print("YES")
    else:
        print("NO")
    t -= 1