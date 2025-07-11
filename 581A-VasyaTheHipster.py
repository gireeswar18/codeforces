red, blue = map(int, input().split())

diff = min(red, blue)
red -= diff
blue -= diff

same = (red // 2)
same += (blue // 2)

print(diff, same)