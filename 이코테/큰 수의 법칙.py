
n, m, k = map(int, input().split())
lst = list(map(int, input().split())).sort(reverse=True)
lst.sort(reverse=True)

first = lst[0]
second = lst[1]
result = 0

## 풀이 1
while True :
    for i in range(k) :
        if m == 0 :
            break
        result += first
        m -= 1
    if m ==0 :
        break
    result += second
    m -= 1

print(result)


## 풀이 2

# cnt = m//(k+1) * k # first 곱한 횟수
# cnt += m%(k+1) * k
#
# result = 0
# result += first * cnt
# result += second * (m-cnt)
#
# print(result)