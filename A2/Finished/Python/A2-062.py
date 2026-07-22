aeiou = ["a","e","i","o","u"]
num = [0,0,0,0,0]
string = input().lower()
for i in range(len(string)):
    if string[i] in aeiou:
        for j in range(5):
            if string[i] == aeiou[j]:
                num[j]+=1
                break
for i in range(5):
    if num[i] == 0:
        continue
    print(aeiou[i]+":",num[i])