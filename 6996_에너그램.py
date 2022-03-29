import sys

t = int(sys.stdin.readline())

for i in range(t) :
   a, b = sys.stdin.readline().split()
   li_a = list(a)
   li_b = list(b)
   # 알파벳순으로 정렬해서 두 문자열이 같으면 곧 A는 B의 에너그램
   li_a.sort(); li_b.sort()

   if li_a == li_b :
      print(a,"&",b,"are anagrams.")
   else :
      print(a,"&",b,"are NOT anagrams.")
