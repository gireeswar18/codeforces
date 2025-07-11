t = int(input())

for _ in range(t):
    points = 0
    mat = []
    for _ in range(10):
        row = str(input())
        mat.append(row)

    for r in range(10):
        for c in range(10):
            if mat[r][c] == 'X':
                if r == 0 or r == 9 or c == 0 or c == 9:
                    points += 1
                elif r == 1 or r == 8 or c == 1 or c == 8:
                    points += 2
                elif r == 2 or r == 7 or c == 2 or c == 7:
                    points += 3
                elif r == 3 or r == 6 or c == 3 or c == 6:
                    points += 4
                else:
                    points += 5

    print(points)