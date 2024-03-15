import math

def land(n,cells):
    # If n and then array is given
    positions = [i for i in range(n) if cells[i] == 1]
    operations = 0

    for i in range(1, len(positions)):
        operations += positions[i] - positions[i - 1] - 1

    return operations
def solve():
        n = int(input())
        cells = list(map(int, input().split()))
        result = land(n, cells)
        print(result)

t = 1
t = int(input())

while t > 0:
    solve()
    t -= 1