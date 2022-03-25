import sys

n = int(sys.stdin.readline())
p = []

for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    p.append([y,x]) # x, y를 바꾸어 sort함수 사용
p.sort()

for i in range(n) :
    print(p[i][1],p[i][0])

