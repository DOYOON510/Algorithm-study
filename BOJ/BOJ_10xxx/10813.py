n, m = map(int, input().split())
n_lst = [i for i in range(n + 1)]
for i in range(m):
    i, j = map(int, input().split())
    n_lst[i], n_lst[j] = n_lst[j], n_lst[i]
for i in range(1, n + 1):
    print(n_lst[i], end=' ')