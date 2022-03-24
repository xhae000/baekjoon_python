import sys

n = int(sys.stdin.readline())
p = []

for _ in range(n) :
    x,y = map(int,sys.stdin.readline().split())
    p.append([x,y])
p.sort() # 각 배열의 첫번째 요소(x)가 1순위, 두번째 요소(y)가 2순위로 정렬됨

for i in p :
    print(i[0],i[1])