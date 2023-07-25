n, b = map(int, input().split())
result = []
num_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# n,b=127,8
while n >= b:
    result.append(num_str[n % b])
    n = n // b
if n != 0:
    result.append(num_str[n])
result.reverse()
print(''.join(map(str, result)))