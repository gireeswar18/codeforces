card = str(input())

choices = list(map(str, input().split()))

res = "NO"
for choice in choices:
    if choice[0] == card[0] or choice[1] == card[1]:
        res = "YES"
        break
print(res)