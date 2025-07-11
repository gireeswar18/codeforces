t = int(input())

for i in range(t):
    word = str(input())
    total = 0
    for j in range(3):
        total += int(word[j])
    
    for j in range(3, 6):
        total -= int(word[j])
    
    print("YES" if total == 0 else "NO")
