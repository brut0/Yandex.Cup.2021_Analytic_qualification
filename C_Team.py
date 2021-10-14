import sys
N, K = map(int, input().split(' '))
lines = sys.stdin.read().splitlines(False)

tasks = []
n = 0
for line in lines:
    n += 1
    tasks.append((int(line[2]), int(line[0]), n))
#tasks.sort()
tasks = sorted(tasks, key=lambda x:(x[0],-x[1]))

output = [[] for _ in range(K)]
busy = [[0, i] for i in range(K)]
success = True
for task in tasks:
    success = False
    busy.sort()
    print(busy)
    for b in busy:
        if b[0] <= task[0] and b[0] + task[1] <= task[0]:
            b[0] += task[1]
            output[b[1]].append(task[2])
            success = True
            break
    if not success:
        break

if success:
    print('YES')
    for o in output:
        print(len(o), *o)
else:
    print('NO')