m = int(input())
n = int(input())
num_lst = []
for x in range(m, n + 1):
    if x <= 1: continue
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: break
    else:
        num_lst.append(x)
if len(num_lst) == 0:
    print(-1)
else:
    print(sum(num_lst))
    print(min(num_lst))