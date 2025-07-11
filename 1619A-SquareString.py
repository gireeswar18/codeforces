t = int(input())

for _ in range(t):
    word = str(input())
    n = len(word)

    if n % 2 == 1:
        print("NO")
        continue

    if word[: n // 2] == word[n // 2 :]:
        print("YES")
    else:
        print("NO")