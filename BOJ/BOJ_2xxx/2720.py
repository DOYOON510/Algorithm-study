t = int(input())
change_lst = [25, 10, 5, 1]

for i in range(t):
    result = []
    c = int(input())
    for change in change_lst:
        result.append(c // change)
        c = c % change

    for j in result:
        print(j, end=' ')