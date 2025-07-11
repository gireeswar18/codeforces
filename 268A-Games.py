n = int(input())

'''
    3
    1 2
    2 4
    3 4

    check if x team's guest uniform matches the other teams' host uniform
'''

lt = []

for i in range(n):
    lt.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(n):
        if i != j and lt[i][1] == lt[j][0]:
            cnt += 1

print(cnt)