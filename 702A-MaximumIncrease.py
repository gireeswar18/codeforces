n = int(input())
arr = list(map(int, input().split()))

longest = 1
curr = 1

for i in range(1, n):
    if arr[i] > arr[i - 1]:
        curr += 1
    else:
        curr = 1
    longest = max(longest, curr)

print(longest)