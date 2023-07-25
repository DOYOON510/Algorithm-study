n = int(input())
line = 1
while n > line:
    n -= line
    line += 1
if line % 2 == 0:
    num1 = n
    num2 = line - n + 1
    print('{}/{}'.format(num1, num2))
else:
    num1 = line - n + 1
    num2 = n
    print('{}/{}'.format(num1, num2))