k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

lt = [0 for _ in range(d)]
res = set()

def fun(x):
    for i in range(x, d + 1, x):
        res.add(i)

fun(k)
fun(l)
fun(m)
fun(n)

print(len(res))