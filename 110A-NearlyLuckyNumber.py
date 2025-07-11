'''
    - Get a num
    - count the 4 and 7
    - check if cnt is lucky
'''

num = int(input())
cnt = 0

while num != 0:
    if num % 10 == 4 or num % 10 == 7:
        cnt += 1
    num //= 10

if cnt == 0:
    print("NO")
    exit()
    
while cnt != 0:
    if cnt % 10 != 4 and cnt % 10 != 7:
        break
    cnt //= 10

print("YES" if cnt == 0 else "NO")