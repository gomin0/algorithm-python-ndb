#성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []
for i in range(n):
    data = input().split()
    array.append((data[0], data[1]))

array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end = ' ')