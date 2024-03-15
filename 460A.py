def solve():
    # If n and then array is given
    n = int(input())
    arr = list(map(int, input().split()))
    val = 1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if len(set([i, j, k, l])) == 4:
                        s= abs(arr[i] - arr[j]) + abs(arr[j] - arr[k]) + abs(arr[k] - arr[l]) + abs(arr[l] - arr[i])
                        val = max(val, val)
    print(val)
t = 1
# t = int(input())

while t > 0:
    solve()
    t -= 1