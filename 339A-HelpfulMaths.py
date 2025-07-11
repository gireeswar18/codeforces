string = str(input())

nums = string.split('+')
nums.sort()

print("+".join(nums))