#국영수

#**튜플은 모든 원소가 첫 번째 원소의 순서에 맞게 정렬되고, 같으면 두번째, 같으면 세번째 원소의 순서로 정렬된다**

n = int(input())

students = []
for _ in range(n):
    students.append(input().split())

'''
[정렬 기준]
1) 두 번째 원소를 기준으로 내림차순
2) 두 번째 원소가 같으면 세 번째 원소를 기준으로 오름차순
3) 세 번째 원소가 같으면 네 번째 원소를 기준으로 내림차순
4) 네 번째 원소가 같으면 첫 번째 원소를 기준으로 오름차순
'''

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])