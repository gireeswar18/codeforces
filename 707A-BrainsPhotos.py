m, n = map(int, input().split())

mat = []

for _ in range(m):
    row = list(map(str, input().split()))
    mat.append(row)

for r in range(m):
    for c in range(n):
        if mat[r][c] == 'C' or mat[r][c] == 'M' or mat[r][c] == 'Y':
            print("#Color")
            exit()

print("#Black&White")