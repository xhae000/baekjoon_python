import sys

n = int(sys.stdin.readline())
s = []
differ = []
result = ""

for _ in range(n) :
    s.append(sys.stdin.readline().rstrip("\n"))

for i in range(len(s[0])):
    c = s[0][i] 
    for j in range(1, n) : 
        if s[j][i] != c :
            differ.append(i)

for i in range(len(s[0])) :
    if i in differ :
        result += '?'
    else : result += s[0][i]
    
print(result)