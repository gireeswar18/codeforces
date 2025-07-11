n = int(input())

skills = list(map(int, input().split()))

skill_cnt = {
    1: [],
    2: [],
    3: []
}

for i, skill in enumerate(skills):
    skill_cnt[skill].append(i + 1)

i = j = k = 0

print(min(len(skill_cnt[1]), len(skill_cnt[2]), len(skill_cnt[3])))

while i < len(skill_cnt[1]) and j < len(skill_cnt[2]) and k < len(skill_cnt[3]):
    print(skill_cnt[1][i], skill_cnt[2][j], skill_cnt[3][k])
    i += 1
    j += 1
    k += 1
