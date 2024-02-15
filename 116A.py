
def solve(n, stops):
    maxi = 0
    current = 0
    
    for i in range(n):
        a, b = stops[i]
        current -= a
        current += b 
        
        maxi = max(maxi, current)
    
    return maxi

n = int(input())
stops = []
for i in range(n):
    ai, bi = map(int, input().split())
    stops.append((ai, bi))

print(solve(n, stops))



t = 1
# t = int(input())

while t > 0:
    solve(n, stops)
    t -= 1