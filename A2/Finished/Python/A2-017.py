s = [60,80]
m = [80,100]
l = [100,120]
inp = input().split()
size,flavor = inp[0],inp[1]
if size == "S":
    if flavor == "R":
        price = s[0]
    elif flavor == "T":
        price = s[1]
elif size == "M":
    if flavor == "R":
        price = m[0]
    elif flavor == "T":
        price = m[1]
elif size == "L":
    if flavor == "R":
        price = l[0]
    elif flavor == "T":
        price = l[1]
top = input().split()
if len(top) > 1:
    if top[0] == "P":
        price+=(15*int(top[1]))
    elif top[0] == "E":
        price+=(10*int(top[1]))
print(price)