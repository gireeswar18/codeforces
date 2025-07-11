t = int(input())

for _ in range(t):
    n = int(input())
    word = str(input())

    # two pointers to check if reduction is possible
    i = 0
    j = n - 1

    while i < j and word[i] != word[j]:
        i += 1
        j -= 1

    print(j - i + 1)