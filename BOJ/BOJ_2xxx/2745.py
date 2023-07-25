## 1
n, b = input().split()
result = 0
num_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, num in enumerate(reversed(n)):
    sum = num_str.index(num) * (int(b) ** i)
    result += sum
print(result)

## 2
n, b = input().split()
print(int(n, base=int(b)))