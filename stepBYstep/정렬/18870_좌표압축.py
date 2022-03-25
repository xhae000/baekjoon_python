import sys

n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))

# 같은 좌표 중복 제거 및 정렬
sort_p = list(sorted(set(p))) 

# list의 index함수를 사용하여 순서를 불러오면 i당 시간 복잡도가 O(n) 이지만,
# 정렬된 값들을 dictionary에 저장해주면 순서를 불러오는 시간 복잡도는 오직 O(1)이다. 
dict_p = {sort_p[i] : i for i in range (len(sort_p))}


# 정렬된 좌표들의 순서 즉 압축된 좌표를 출력
for i in p :
    print(dict_p.get(i), end=" ")
