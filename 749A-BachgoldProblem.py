n = int(input())

twos = n // 2

print(twos)

if n % 2 == 0:
    for _ in range(twos):
        print(2, end = " ")
else:
    for _ in range(twos - 1):
        print(2, end = " ")
    print(3)