t = int(input())

for _ in range(t):
    n = int(input())
    dirs = str(input())

    x = 0
    y = 0
    res = False

    for dir in dirs:
        if dir == 'U':
            y += 1
        elif dir == 'D':
            y -= 1
        elif dir == 'L':
            x -= 1
        else:
            x += 1

        if x == 1 and y == 1:
            res = True
            break
    
    print("YES" if res else "NO")