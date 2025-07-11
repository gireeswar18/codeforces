n, m = map(int, input().split())
left = False

lt = [['.' for _ in range(m)] for _ in range(n)]

for i in range(n):
    if i % 2 != 0:
        if left:
            lt[i][0] = '#'
        else:
            lt[i][m - 1] = '#'

        left = not left 
        continue
    
    for j in range(m):
        lt[i][j] = '#'

for i in range(n):
    for j in range(m):
        print(lt[i][j], end = "")
    print()