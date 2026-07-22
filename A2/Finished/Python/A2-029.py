height = int(input())
triangle = []
for i in range(height):
    placeholder = []
    for j in range(i+1):
        if j == 0 or j == i:
            placeholder.append(0)
        elif i == height-1:
            placeholder.append(0)
        else:
            placeholder.append(1)
    triangle.append(placeholder)
for i in range(height):
    print(*triangle[i])