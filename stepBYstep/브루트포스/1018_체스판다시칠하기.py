import sys

y,x = map(int,sys.stdin.readline().split())
c = [['']*x]*y
result = []

for i in range(y) :
    c[i] = list(sys.stdin.readline().rstrip('\n'))

for i in range(y-7) :
    for j in range(x-7) :
         cnt = [0,0] # cnt[0]은 맨 처음이 흰 색인 경우, cnt[0]은 검정색인 경우이다
         for k in range(i,i+8) :
             for l in range(j,j+8) :
                 # 만약에 흰색으로 시작했다면, 체스판의 행과 열의 합이 짝수일때 흰색이다
                 # 이 규칙을 찾는게 가장 중요.
                 if (k+l)%2 == 0 : # 처음의 색상과 다르면 고침
                     if c[k][l] !='W' : # 처음이 흰색인 경우
                        cnt[0]+=1
                     if c[k][l] !='B' : # 처음이 검정색인 경우
                         cnt[1]+=1
                 else : # 처음의 색상과 같으면 고침
                     if c[k][l] !='W' : #처음이 흰색인 경우
                         cnt[1] += 1 
                     if c[k][l] != 'B' : #처음이 검정색인 경우
                         cnt[0] += 1
         result.append(min(cnt)) 
print(min(result))
 