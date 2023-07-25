n = int(input())
result = 4
for i in range(n):
    result = int(((result ** (1 / 2) * 2) - 1) ** 2)
print(result)