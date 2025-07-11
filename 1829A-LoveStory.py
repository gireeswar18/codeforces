t = int(input())

for i in range(t):
    word = str(input())
    og = "codeforces"
    cnt = 0

    for i in range(10):
        if og[i] != word[i]:
            cnt += 1
        
    print(cnt)