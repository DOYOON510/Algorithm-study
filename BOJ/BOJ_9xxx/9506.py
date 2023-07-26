while True:
    n = int(input())
    n_lst = []
    if n == -1:
        break
    else:
        for i in range(1, n):
            if n % i == 0:
                n_lst.append(i)
    if sum(n_lst) == n:
        print('{} = '.format(n), end='')
        print(*n_lst, sep=' + ')
    else:
        print('{} is NOT perfect'.format(n))