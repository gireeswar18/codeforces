n = int(input())
word = str(input()).lower()

print("YES" if len(set(word)) == 26 else "NO")