t = int(input())
w = "Timur"
check = set(w)

for i in range(t):
    n = int(input())
    name = str(input())

    if n != 5:
        print("NO")
        continue

    if set(name) == check:
        print("YES")
    else:
        print("NO")