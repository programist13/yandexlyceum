a1 = open('input.txt', 'r')
b1 = open('output.txt', 'w')
nums = a1.read().splitlines()
for i in range(len(nums)):
    nums[i] = nums[i].split()
print(nums)
m = int(nums[0][0])
a = int(nums[0][1])
b = int(nums[0][2])
counter = int(nums[1][0])
count = 0
print(m)
print(a)
print(b)
print(counter)
nums.pop(0)
nums.pop(0)
print(nums)
for i in nums:
    z = int(i[0])
    s = int(i[1])
    n = int(i[2])
    if z == 1:
        for i in range(n):
            s = int((a * s + b) % m)
        b1.write(str(s) + '\n')
    elif z == 2:
        count = 0
        for i in range(m):
            count += 1
            s = (a * s + b) % m
            if s == n:
                break
        if s == n:
            b1.write(str(count) + '\n')
        else:
            b1.write('-1' + '\n')
b1.close()
