initial_pos = str(input())
instructions = str(input())

pos = 0

for c in instructions:
    if c == initial_pos[pos]:
        pos += 1
    
print(pos + 1)