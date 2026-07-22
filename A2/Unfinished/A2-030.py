line = []
count = 0
for i in range(5):
    inp = input().split()
    for j in range(5):
        inp[j] = int(inp[j])
    line.append(inp)
for i in range(5):
    lasty,lastx = i,0
    cur = 0
    for j in range(5):
        if line[i][j] != 0:
            cur+=line[i][j]
            lastx = j
    if cur%2 != 0:
        count+=1
        print(lasty,lastx+1)
if count == 0:
    print("-1 -1")