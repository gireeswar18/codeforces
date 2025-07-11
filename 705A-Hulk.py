layers = int(input())

LOVE = "I love"
HATE = "I hate"

res = []

for i in range(1, layers + 1):
    if i % 2 == 1:
        res.append(HATE)
    else:
        res.append(LOVE)

    res.append("that")

res[-1] = "it"

print(" ".join(res))