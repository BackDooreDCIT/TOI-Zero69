W, H, M, N = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
widths = []
prev = 0
for x in X:
    widths.append(x - prev)
    prev = x
widths.append(W - prev)
heights = []
prev = 0
for y in Y:
    heights.append(y - prev)
    prev = y
heights.append(H - prev)
largest = 0
second = 0
for w in widths:
    for h in heights:
        area = w * h
        if area > largest:
            second = largest
            largest = area
        elif area > second:
            second = area
print(largest, second)