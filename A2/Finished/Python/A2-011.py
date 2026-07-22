old = input().split()
new = []
for i in range(len(old)):
    if old[i] not in new:
        new.append(old[i])
print(*new)