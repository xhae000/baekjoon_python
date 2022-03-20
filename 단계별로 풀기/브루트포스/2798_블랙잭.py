import sys

n,m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
result = 0

for i in card :
    for j in card :
        for k in card :
            if k==i or k==j or i==j : continue
            if(result < i+j+k <= m) :
                result = i+j+k

print(result)