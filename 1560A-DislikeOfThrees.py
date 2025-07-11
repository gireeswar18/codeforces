t = int(input())

for i in range(t):
    k = int(input())

    num = 1
    while k != 0:
        if num % 3 != 0 and num % 10 != 3:
            k -= 1
        if k == 0:
            break
        num += 1

    
    print(num)
