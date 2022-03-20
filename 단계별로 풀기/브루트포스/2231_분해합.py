import sys

n = int(sys.stdin.readline()) 
c = 0
c_list = [0]*7 #최대로 검사할 수 있는 c는 1,000,000 이므로 7자리 배열을 만든다
result = 0

while c<n : 
    c += 1
    for i in range(len(str(c))) : #각 자리의 수들을 c_list에 저장
        c_list[i] = int(str(c)[i])

    if c+sum(c_list) == n : 
        #생성자가 맞는지 검사, 최소의 생성자를 구하는 문제기에 최초의 생성자를 찾으면 바로 break
        result = c
        break
print(result) #n이 생성자가 없는 수였다면 0이 출력된다.

