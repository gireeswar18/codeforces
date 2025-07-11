n = int(input())

cnt = 0
prev = 0

for i in range(n):
    mag = int(input())
    if prev != mag:
        prev = mag
        cnt += 1
    
print(cnt)