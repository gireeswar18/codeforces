dest = int(input())
steps = 0

jump = 5

while dest != 0:
    if dest < jump:
        jump -= 1
    else:
        steps += (dest // jump)
        dest = dest % jump

print(steps)