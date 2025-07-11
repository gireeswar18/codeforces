str1 = str(input()).lower()
str2 = str(input()).lower()

def fun():
    for i in range(len(str1)):
        a = ord(str1[i])
        b = ord(str2[i])

        if a < b:
            return -1

        elif b < a:
            return 1
        
    return 0
    
print(fun())