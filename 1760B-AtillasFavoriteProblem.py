t = int(input())

for _ in range(t):
    n = int(input())
    word = str(input())

    max_val = ord('a')

    for c in word:
        max_val = max(max_val, ord(c))

    print(max_val - ord('a') + 1)