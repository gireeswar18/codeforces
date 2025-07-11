sentence = str(input())

sentence = sentence[1:len(sentence) - 1]

uniq = set()

ind = 0
n = len(sentence)

while ind < n:
    if sentence[ind].isalpha():
        uniq.add(sentence[ind])
    ind += 1

print(len(uniq))