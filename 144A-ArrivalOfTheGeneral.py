'''

find the min one from right
find the max one from left

'''

min_ht = 200
min_ht_ind = -1

max_ht = 0
max_ht_ind = -1

n = int(input())
heights = list(map(int, input().split()))

for i in range(n - 1, -1, -1):
    if heights[i] < min_ht:
        min_ht = heights[i]
        min_ht_ind = i
    
for i in range(n):
    if heights[i] > max_ht:
        max_ht = heights[i]
        max_ht_ind = i

res = n - 1 - min_ht_ind + max_ht_ind
if min_ht_ind < max_ht_ind:
    res -= 1
print(res)