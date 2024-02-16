import math

def solve():
    # If n and then array is given
    n = int(input())
    value = [int(x) for x in input().split()]
    value.sort()
    total=sum(value)
"""
n
divide into 4 parts such that all the elements are distinct
first two part and second two parts should be equal
every array is of length 4 only


approach:
    20
        1 1 9 9
        2 2 8 8
        3 3 7 7
        4 4 6 6
        5 5 5 5
    6
        1 1 2 2
        2 2 1 1
    temp = n
    I will decrease the temp by two everytime until it becomes 0
    

"""    
def solve2():
    n = int(input())
    if n-2 <=0 or n%2==1:
        print(0)
        return
    
    length = 1
    width = (n-2*length)/2
    count = 0

    while (length != width and width > 1):
        count+=1
        length +=1
        width = (n-2*length)/2
    print(count)
    return

solve2()