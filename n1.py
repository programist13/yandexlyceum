with open('input.txt', 'r') as f:
    nums = f.read().splitlines()
n = int(nums[0])
z = open('output.txt', 'w')
a = nums[1]
a = a.split()
counter = 0
count = 0
sett = []
for i in range(n):
    sett.append(int(a[count]))
    count += 1
print(sett)
sett.sort()
print(sett)
h = max(sett)
while True:
    sett[0] += 1
    sett[1] += 1
    counter += 1
    print(sett)
    sett.sort()
    print(sett)
    print('============')
    if sett[0] == sett[-1]:
        z.write(str(counter))
        z.close()
        break
    if sett[-1] == h + 2:
        z.write('-1')
        z.close()
        break
        
