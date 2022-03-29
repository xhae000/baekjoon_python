import sys

t = int(sys.stdin.readline())

for i in range(t) :
   a = list(sys.stdin.readline().rstrip("\n"))
   a[0] = a[0].upper()

   print(''.join(a))