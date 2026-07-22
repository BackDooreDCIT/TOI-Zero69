pyramid = []
inp = input().split()
base = int(inp[0])
take = int(inp[1])
curbase = base
while curbase != 0:
    temp = curbase*curbase
    pyramid.append(temp)
    temp = 0
    curbase-=1
pyramid.sort()
for i in range(len(pyramid)):
    if take>pyramid[0]:
        take-=pyramid[0]
        pyramid.pop(0)
    elif take == pyramid[0]:
        take-=pyramid[0]
        pyramid.pop(0)
    else:
        pyramid[0]-=take
        take = 0
print(len(pyramid))