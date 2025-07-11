lt = list(map(int, input().split()))

total = max(lt)

for num in lt:
    if num != total:
        print(total - num, end=" ")