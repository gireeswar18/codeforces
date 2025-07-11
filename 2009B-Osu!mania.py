t = int(input())

for _ in range(t):
    n = int(input())

    arr = []
    for _ in range(n):
        row = str(input())
        arr.append(row)
    
    for r in range(n - 1, -1, -1):
        for i, c in enumerate(arr[r]):
            if c == '#':
                print(i + 1, end = " ")
                break
    
    print()