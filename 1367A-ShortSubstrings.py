t = int(input())

for i in range(t):
    word = str(input())

    res = []

    for j in range(len(word)):
        if j % 2 == 0:
            res.append(word[j])

    
    res.append(word[-1])

    print("".join(res))