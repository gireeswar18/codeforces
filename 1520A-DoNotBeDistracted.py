t = int(input())

for _ in range(t):
    n = int(input())
    word = str(input())

    char_set = set()
    ind = 0

    while ind < n:
        key = word[ind]
        if key in char_set:
            print("NO")
            break
        
        char_set.add(key)
        while ind < n and word[ind] == key:
            ind += 1

    if ind == n:
        print("YES")