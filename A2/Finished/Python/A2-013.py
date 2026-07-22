Rtype = [12,18,25]
Ttype = [15,20,30]
Mtype = [10,15,20]
bub = input().split()
bubcal = 0
if bub[0] == 'H':
    bubcal = int(bub[1])*5
elif bub[0] == 'O':
    bubcal = int(bub[1])*3
elif bub[0] == 'J':
    bubcal = int(bub[1])*2

tea = input().split()
teacal = 0
if tea[0] == 'R':
    teacal = int(tea[2])*Rtype[int(tea[1])-1]
elif tea[0] == 'T':
    teacal = int(tea[2])*Ttype[int(tea[1])-1]
elif tea[0] == 'M':
    teacal = int(tea[2])*Mtype[int(tea[1])-1]
print(teacal+bubcal)