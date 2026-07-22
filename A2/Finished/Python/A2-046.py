amount = int(input())
vowel = ["a","e","i","o","u"]
for i in range(amount):
    max_cons = 0
    curcons = 0
    vowcount = 0
    inp = input().lower()
    # print(inp)
    for j in range(len(inp)):
        if inp[j] in vowel:
            curcons+=1
            vowcount+=1
        elif inp[j] not in vowel or inp[j] == " ":
            if curcons > max_cons:
                max_cons = curcons
                curcons = 0
            else:
                curcons = 0
        # print("curcons",curcons)
        # print("max_cons",max_cons)
        # print("vowcount",vowcount)
    if curcons > max_cons:
        max_cons = curcons
    print("Line",str(int(i+1))+":","vowels =",str(vowcount)+",","max_consecutive =",max_cons)