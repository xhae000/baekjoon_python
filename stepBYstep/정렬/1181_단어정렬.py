import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n) :
    w = sys.stdin.readline().rstrip("\n")
    # sort 함수로 단어의 길이를 기준으로 정렬하기 위해 길이와 함께 저장
    words.append([len(w),w])

# 단어의 중복을 제거하기 위해 list -> turple -> set -> list 의 과정을 거침
words = list(set(list(map(tuple,words))))
words.sort()

for i in range(len(words)) :
    print(words[i][1])