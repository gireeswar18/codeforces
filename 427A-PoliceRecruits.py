n = int(input())

lt = list(map(int, input().split()))

police = 0
crimes = 0

for i in lt:
    if i != -1:
        police += i
    else:
        if police != 0:
            police -= 1
        else:
            crimes += 1

print(crimes) 