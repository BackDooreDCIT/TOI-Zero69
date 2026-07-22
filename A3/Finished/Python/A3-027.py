inp = input().split()
zmap = []
newmap = []

# print(inp)
for i in range(int(inp[0])):
    tempmap = input().split()
    zmap.append(tempmap)
    newmap.append(tempmap[:])

# print('zmap:', zmap)
# print('newmap:', newmap)

# print('===== START for loop =====')
for i in range(int(inp[0])):
    # print('len(zmap):', len(zmap)-1, 'i:', i)

    if i == len(zmap)-1:
        break
    else:
        for j in range(int(inp[1])):
            # print(f'zmap[{i}][{j}]')
            if zmap[i][j] == '*':
                newmap[i+1][j] = '*'
#                 print('zmap after adding * :', zmap)
#                 print('newmap after adding *:', newmap)

# print('===== END for loop =====')

# print(newmap)
# print("---newmap-----")
for i in range(int(inp[0])):
    print(*newmap[i])
# print("oldmap----------------")
# for i in range(int(inp[0])):
#     print(*zmap[i])