amount = int(input())
scores = input().split()
students = []
properstudent = []
for i in range(len(scores)):
    students.append("Student"+str(int(i+1)))
    properstudent.append("Student "+str(int(i+1)))
    scores[i] = int(scores[i])
highest = max(scores)
lowest = min(scores)
average = sum(scores)/len(scores)
# print(highest,lowest,average)
print("Student:", *students)
print("Highest score:",highest)
print("Lowest score:",lowest)
print(f"Average score: {average:.1f}")
print("Students who scored above average:")
for i in range(len(scores)):
    if scores[i] > average:
        print(properstudent[i])