# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    score2 = set(score)
    score3 = [i for i in score2]
    count = [0] * len(score3)
    for i in range(len(score3)):
        count[i] = score.count(score3[i])
    result_index = count.index(max(count))
    print('#{} {}'.format(test_case, score3[result_index]))


