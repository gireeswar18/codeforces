t = int(input())

for i in range(t):
    n = int(input())
    word = str(input())
    res = 0

    mp = [0 for _ in range(26)]

    for c in word:
        key = ord(c) - ord('A')
        if mp[key] == 0:
            res += 2
        else:
            res += 1

        mp[key] += 1

    print(res)