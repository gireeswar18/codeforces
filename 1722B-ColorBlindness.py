t = int(input())

for _ in range(t):
    n = int(input())
    row1 = list(str(input()))
    row2 = list(str(input()))

    for i in range(n):
        if row1[i] == 'B':
            row1[i] = 'G'

    for i in range(n):
        if row2[i] == 'B':
            row2[i] = 'G'
        
    if ("".join(row1) == "".join(row2)):
        print("YES")
    else:
        print("NO")