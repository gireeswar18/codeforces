t = int(input())

for i in range(t):
    n = int(input())
    half = n // 2
    lt = []
    val = 2
    even_sum = 0

    if half % 2 == 1:
        print("NO")
        continue

    for j in range(half):
        lt.append(val)
        even_sum += val
        val += 2
    
    val = 1
    for j in range(half - 1):
        lt.append(val)
        even_sum -= val
        val += 2

    lt.append(even_sum)

    print("YES")
    for x in lt:
        print(x, end=" ")
    print()