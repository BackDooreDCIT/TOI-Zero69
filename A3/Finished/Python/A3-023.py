# this only got an 80/100 which is considered a pass, but i could probably optimize it better (which i will not do)

A, B = map(int, input().split())
maxi = 3 * B
yesprimexiz = [True] * (maxi + 1)
yesprimexiz[0] = yesprimexiz[1] = False
for i in range(2, int(maxi ** 0.5) + 1):
    if yesprimexiz[i]:
        for j in range(i * i, maxi + 1, i):
            yesprimexiz[j] = False
primexiz = []
for i in range(2, maxi + 1):
    if yesprimexiz[i]:
        primexiz.append(i)
ans = 0
for p in primexiz:
    if p < 3 * A:
        continue
    if p > 3 * B:
        break
    for a in range(A, B + 1):
        L = max(a, p - a - B)
        R = (p - a) // 2
        if L <= R:
            ans += (R - L + 1)
print(ans)