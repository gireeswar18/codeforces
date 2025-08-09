t = int(input())

for _ in range(t):
    ip = str(input())

    freq = [0 for _ in range(26)]
    cnt = 0

    for c in ip:
        freq[ord(c) - ord('a')] += 1

    for f in freq:
        if f > 0:
            cnt += 1
    
    if cnt == 1:
        print("NO")
    else:
        print("YES")

        res = []
        n = len(ip)
        for i in range(n // 2):
            res.append(ip[i])
            res.append(ip[n - i - 1])

        if n % 2 == 1:
            res.append(ip[n // 2])

        op = "".join(res)
        if op == ip:
            op = "".join(reversed(res))
        print(op)