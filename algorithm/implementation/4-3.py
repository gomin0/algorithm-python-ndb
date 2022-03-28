#왕실의 나이트

data = input()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

count = 0

steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]

for step in steps:
    nx = column + step[0]
    ny = row + step[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)