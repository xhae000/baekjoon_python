import sys

t = int(sys.stdin.readline())
result = []

for i in range(t) :
   a, b = sys.stdin.readline().rstrip("\n").split()
   temp_a = []
   for j in a :
      if j in b : 
         temp_a.append(j)
   if list(a) == temp_a :
      result.append(a+" & "+b+" are anagrams.")
   else :
      result.append(a+" & "+b+" are NOT anagrams.")

print("\n".join(result))