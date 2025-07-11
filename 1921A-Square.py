t = int(input())

for _ in range(t):
    pts = []
    for _ in range(4):
        pt = list(map(int, input().split()))
        pts.append(pt)
    
    sides = set()

    for pt in pts:
        sides.add(pt[0])

    print((max(sides) - min(sides)) ** 2)