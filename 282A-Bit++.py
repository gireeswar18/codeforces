t = int(input())
res = 0
for i in range(t):
    op = str(input())
    if op[0] == '+' or op[2] == '+':
        res += 1
    else:
        res -= 1

print(res) 