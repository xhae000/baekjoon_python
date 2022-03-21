""" 이 문제는 메모리가 8MB 제한이라 이전과 같이 sort 함수로는 해결할 수 없었고
 입력 받은 숫자를 세는 방법으로 해결할 수 있었다.
"""
import sys

n = int(sys.stdin.readline())
# 입력 받을 수 있는 수의 크기만큼 할당
# 최댓값이 10000인데 10001개를 할당해준 이유는 배열은 0부터 시작하는데 문제에서의 최솟값은 1이기 때문
num = [0]*10001

for _ in range (n) :
    a = int(sys.stdin.readline())
    num[a] += 1

for i in range(10001) :
    if i!=0 :
        for j in range(num[i]) :
            print(i)