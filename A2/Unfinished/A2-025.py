zmap = []
size = input().split()
for i in range(int(size[0])):
    placeholder = []
    for j in range(int(size[1])):
        placeholder.append(0)
    zmap.append(placeholder)
# print(zmap)
rabpos = input().split()
# zmap[int(rabpos[0])][int(rabpos[1])] = "x"
# print(zmap)
amount = int(input())
for i in range(amount):
    inp = input().split()
    zmap[int(inp[0])][int(inp[1])] = "x"
