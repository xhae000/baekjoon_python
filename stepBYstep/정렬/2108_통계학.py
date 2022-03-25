import sys
import statistics as stt
# 이 문제는 파이썬에서 지원하는 statistics 라이브러리를 사용하면 쉽게 해결된다

n = int(sys.stdin.readline())
a = []

for i in range (n) :
    a.append(int(sys.stdin.readline()))

# 최빈값이 여러개인 경우 두번째로 작은 값을 찾기
mm = stt.multimode(a)
if len(mm) != 1 :
    mm.remove(min(mm))
mm = min(mm)

print(round(stt.mean(a)))
print(stt.median(a))
print(mm)
print(max(a)-min(a))