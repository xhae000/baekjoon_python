import sys

n = sys.stdin.readline().rstrip("\n")
result = "NO"

if len(n) != 1  :
    for i in range(len(n)) :
        a = list(n[:i])
        b = list(n[i:])

        mul_a = 1
        mul_b = 1

        for i in a : mul_a *= int(i)
        for i in b : mul_b *= int(i)
        
        if mul_a==mul_b : result="YES";break


print(result)
   
