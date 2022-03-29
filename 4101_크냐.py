import sys

a = 1; b=0

while 1 :
    a, b= map(int, sys.stdin.readline().split())
    if a==b==0 : break
    if a>b : print("Yes")
    else : print("No")  