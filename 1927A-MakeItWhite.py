t = int(input())

for _ in range(t):
    n = int(input())
    word = str(input())
    st = n
    end = -1

    for i in range(n):
        if word[i] == 'B':
            st = min(st, i)
            end = max(end, i)
    
    print(end - st + 1)