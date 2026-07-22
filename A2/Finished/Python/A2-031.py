wrongpos = 0
length = int(input())
li1 = input().split()
li2 = input().split()
looptime = int(input())
for i in range(looptime):
    inp = input().split()
    if int(inp[0]) == 1:
        li1[int(inp[1])] = inp[2]
    elif int(inp[0]) == 2:
        li2[int(inp[1])] = inp[2]
for i in range(length):
    if ((li1[i] == "A" and li2[i] != "T") or (li1[i] == "T" and li2[i] != "A")) or ((li1[i] == "C" and li2[i] != "G") or (li1[i] == "G" and li2[i] != "C")):
        wrongpos+=1
print(*li1)
print(*li2)
print(wrongpos)