li = []
one = int(input())
print("Input number 1 stored.")
two = int(input())
print("Input number 2 stored.")
three = int(input())
print("Input number 3 stored.")
li.append(one)
li.append(two)
li.append(three)
og = li[:]
cmd = int(input())
if cmd == 1:
    print("Original order:",*og)
elif cmd == 2:
    li.sort(reverse=True)
    print("Descending order:",*li)
elif cmd == 3:
    li.sort()
    print("Ascending order:",*li)