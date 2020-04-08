import sys

height = []
for i in sys.stdin.readlines():
    height.append(int(i.rstrip()))
total = 0
count = 0
if len(height) == 0:
    print('-1')
else:
    for i in height:
        total += i
        count += 1
    print(total / count)
