n, x = map(int, input().split())
n_lst = list(map(int, input().split()))
for i in n_lst:
    if i < x:
        print(i, end=' ')