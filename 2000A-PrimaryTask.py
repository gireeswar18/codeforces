t = int(input())

for _ in range(t):
    n = str(input())
    
    if len(n) < 3:
        print("NO")
        continue

    num = n[:2]
    exp = n[2:]

    if num != "10" or exp[0] == '0' or int(exp) < 2:
        print("NO")
    else:
        print("YES") 