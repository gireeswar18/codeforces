levels = int(input())

mp = [0 for _ in range(levels + 1)]

x = list(map(int, input().split()))
y = list(map(int, input().split()))

for x_ind in range(1, x[0] + 1):
    mp[x[x_ind]] = 1 
for y_ind in range(1, y[0] + 1):
    mp[y[y_ind]] = 1 

print("I become the guy." if levels - sum(mp) == 0 else "Oh, my keyboard!")