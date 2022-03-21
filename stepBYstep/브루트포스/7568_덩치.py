import sys

n = int(sys.stdin.readline())
x=[0]*n
y=[0]*n
rank=[1]*n


for i in range(n) :
    x[i],y[i] = map(int,sys.stdin.readline().split())

for i in range(n) :
    for j in range(n) :
        if x[i]<x[j] and y[i]<y[j] :
            rank[i] += 1        

print(" ".join(map(str,rank)))


# 1 1 4 1 0