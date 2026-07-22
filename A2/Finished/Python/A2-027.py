top = -1
topamount = 0
time = int(input())
for i in range(time):
    inp = int(input())
    if inp > top:
        top = inp
        topamount = 1
    elif inp == top:
        topamount+=1
print(top)
print(topamount)