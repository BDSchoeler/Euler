import math
nums={4,8,9}
for i in range(2,101):
    for j in range(2,101):
        nums.add(math.pow(i,j))
print(len(nums))
