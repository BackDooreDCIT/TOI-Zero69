map1 = []
map2 = []
newmap = []
size = input().split()
for i in range(int(size[0])):
    inp = list(input())
    map1.append(inp)
for i in range(int(size[0])):
    inp = list(input())
    map2.append(inp)

for i in range(int(size[0])):
    placeholder = ''
    for j in range(int(size[1])):
        if map1[i][j] == '-' and map2[i][j] == '-':
            placeholder+='-'
        elif (map1[i][j] == '-' and map2[i][j] == '+') or (map1[i][j] == '+' and map2[i][j] == '-'):
            placeholder+='+'
        elif (map1[i][j] == '-' and map2[i][j] == 'x') or (map1[i][j] == 'x' and map2[i][j] == '-'):
            placeholder+='x'
        elif (map1[i][j] == 'x' and map2[i][j] == '+') or (map1[i][j] == '+' and map2[i][j] == 'x'):
            placeholder+='*'
        else:
            placeholder+=map1[i][j]
    print(placeholder)

# for i in range(int(size[0])):
#     print(*newmap[i])