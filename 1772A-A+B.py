t = int(input())

for _ in range(t):
    string = str(input())

    print((ord(string[0]) - ord('0')) + (ord(string[2]) - ord('0')))