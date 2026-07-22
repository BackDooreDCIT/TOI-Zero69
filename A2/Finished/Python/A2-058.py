inp = input().split()
a = int(inp[0])
b = int(inp[1])
d = int(inp[2])
r = int(inp[3])
output = 0
for i in range(a, b+1):
    if i%d == r:
        output+=1
print(output)