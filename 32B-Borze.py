word = str(input())

res = []
ind = 0

while ind < len(word):
    if word[ind] == '.':
        res.append('0')
        ind += 1
    elif word[ind + 1] == '.':
        res.append('1')
        ind += 2
    else:
        res.append('2')
        ind += 2

print("".join(res))