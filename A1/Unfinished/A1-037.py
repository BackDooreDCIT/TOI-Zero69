num = input()
cur = 0
output = ""
for i in range(len(num)-1, -1, -1):
    if i == 3:
        for j in range(int(num[i])):
            if cur != int(num[i]):
                output+="M"
                cur+=1
            else:
                break
        cur = 0
    elif i == 2:
        for j in range(int(num[i])):
            if cur != int(num[i]):
                if int(num[i]) >= 5 and cur < 5:
                    output+="D"
                    cur+=5
                elif int(num[i]) == 4:
                    output+= "CD"
                    cur+=4
                else:
                    output+="C"
                    cur+=1
            else:
                break
        cur = 0
    elif i == 1:
        for j in range(int(num[i])):
            if cur != int(num[i]):
                if int(num[i]) >= 5 and cur < 5:
                    output+="L"
                    cur+=5
                elif int(num[i]) == 4:
                    output+="XL"
                    cur+=4
                else:
                    output+="X"
                    cur+=1
            else:
                break
        cur = 0
    elif i == 0:
        if len(num) == 1 and len(num) == 0:
            output+=0
            break
        for j in range(int(num[i])):
            if cur != int(num[i]):
                if int(num[i]) >= 5 and cur < 5:
                    output+="V"
                    cur+=5
                elif int(num[i]) == 4:
                    output+="IV"
                    cur+=4
                else:
                    output+="I"
                    cur+=1
            else:
                break
        cur = 0
print(output)