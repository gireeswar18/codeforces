n, ic = map(int, input().split())

distressed = 0

for _ in range(n):
    ip = str(input())
    num = int(ip[2:])

    if ip[0] == '+':
        ic += num
    else:
        if ic >= num:
            ic -= num
        else:
            distressed += 1

print(ic, distressed)