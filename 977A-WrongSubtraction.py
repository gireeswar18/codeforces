num, k = map(int, input().split())

while k != 0:
    if num % 10 != 0:
        num -= 1
    else:
        num //= 10
    k -= 1

print(num)