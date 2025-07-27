t = int(input())

for _ in range(t):
    ip = str(input())

    res = [ip[0]]

    for i, c in enumerate(ip):
        if c == ' ':
            res.append(ip[i + 1])

    print("".join(res))