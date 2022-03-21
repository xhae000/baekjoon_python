import sys

n = int(sys.stdin.readline())
num = []

for _ in range (n) :
    a = int(sys.stdin.readline())
    num.append(a)

num.sort()

print("\n".join(map(str,num)))