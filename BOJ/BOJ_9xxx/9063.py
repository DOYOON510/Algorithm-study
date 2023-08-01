n = int(input())
x_lst = []
y_lst = []
for i in range(n):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
if n == 1:
    print(0)
else:
    x_min, x_max, y_min, y_max = min(x_lst), max(x_lst), min(y_lst), max(y_lst)
    x2 = x_max - x_min
    y2 = y_max - y_min
    print(x2 * y2)

