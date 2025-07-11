n = int(input())
'''

4 ->
minus = 1, 3 -> 4
add = 2, 4 -> 6

6 ->
+ -> 2 4 6 = 12 (n * (n + 1)), n = 3
- -> 1 3 5 = 9 (n * n), n = 3

5 ->
+ -> 2 4 -> 6 [n * (n + 1)], n = 2
- -> 1 3 5 -> 9 [n * n], n = 3

'''

add = 0
sub = 0
cnt = n // 2

if n % 2 == 0:
    sub = cnt * cnt
else:
    sub = (cnt + 1) * (cnt + 1)

add = cnt * (cnt + 1)

print(add - sub)