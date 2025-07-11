n, k = map(int, input().split())

time_taken = 0

for i in range(1, n + 1):
    time_taken += (5 * i)

    if time_taken + k > 240:
        print(i - 1)
        quit()

print(n)