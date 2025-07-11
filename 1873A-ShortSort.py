t = int(input())

res = {
    "abc": "YES",
    "acb": "YES",
    "bac": "YES",
    "bca": "NO",
    "cab": "NO",
    "cba": "YES"
}

for i in range(t):
    word = str(input())
    print(res[word])