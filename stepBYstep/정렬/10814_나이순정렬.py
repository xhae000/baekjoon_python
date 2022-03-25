import sys

n = int(sys.stdin.readline())
custom = []

for i in range(n) :
    age, name = map(str,sys.stdin.readline().split())
    # 정렬 기준이 1순위가 나이, 2순위가 가입 순서이기 때문에 i와 함께 저장
    custom.append([int(age),i,name])

custom.sort()

for i in range(n) :
    print(custom[i][0], custom[i][2])
