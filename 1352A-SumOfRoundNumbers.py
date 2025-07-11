t = int(input())

for i in range(t):
    num = int(input())
    lt = []
    fact = 1

    while num != 0:
        d = num % 10
        if d != 0:
            lt.append(d * fact)
        
        fact = fact * 10
        num //= 10
    
    print(len(lt))
    for x in reversed(lt):
        print(x, end = " ")
    print()