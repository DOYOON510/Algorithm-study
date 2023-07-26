n, k = map(int, input().split())
n_lst = []
for i in range(1,n+1):
    if n % i == 0:
        n_lst.append(i)

if len(n_lst) >= k:
    print(n_lst[k - 1])
else:
    print(0)