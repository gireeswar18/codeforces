def helper():
    word = str(input().strip())
    n = len(word)
    if n > 10:
        print(len(word[1: n - 1]), end="") 
        print(word[n - 1])
    else:
        print(word)

t = int(input())
for i in range(t):
    helper()