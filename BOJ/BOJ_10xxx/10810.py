# 내 코드
n, m = map(int, input().split())
n_lst = [0] * n
for lst in range(m):
    i, j, k = map(int, input().split())
    k_lst = [k] * (j - i + 1)
    n_lst[i - 1:j] = k_lst

for i in n_lst:
    print(i, end=' ')
# result=' '.join(map(str,n_lst))
# print(result)

# 다른 코드
n, m = map(int, input().split())
n_lst = [0] * n
for lst in range(m):
    i, j, k = map(int, input().split())
    for num in range(i - 1, j):
        n_lst[num] = k

for n in range(n):
    print(n_lst[n], end=' ')