a = str(input())
b = str(input())

def fun():
    if len(a) != len(b):
        return "NO"
    
    i, j = 0, len(b) - 1

    while j >= 0:
        if a[i] != b[j]:
            return "NO"
        i += 1
        j -= 1
    
    return "YES"

print(fun())