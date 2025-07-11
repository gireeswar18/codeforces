a = str(input())
b = str(input())
c = str(input())

mp = {}

for l in a:
    mp[l] = mp.get(l, 0) + 1
for l in b:
    mp[l] = mp.get(l, 0) + 1

for l in c:
    mp[l] = mp.get(l , 0) - 1

for l in mp:
    if mp[l] != 0:
        print("NO")
        quit()

print("YES")