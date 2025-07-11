n = int(input())

# to whom he gave - i/p
# given by - o/p

lt = list(map(int, input().split()))

# 2 3 4 1

'''
2 -> 1
3 -> 2
4 -> 3
1 -> 4

4 1 2 3

1 3 2
1 -> 1
3 -> 2
2 -> 3
'''

res = [0 for _ in range(n)]
for i in range(n):
    res[lt[i] - 1] = i + 1

for x in res:
    print(x, end=" ")
print()