mat = []
for i in range(5):
    lt = list(map(int, input().split()))
    mat.append(lt)

for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            print(abs(2 - i) + abs(2 - j))