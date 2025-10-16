
n, m = map(int, input().split())

for i in range(n):
    data = list(map(int, input().split()))
    result = 0
    result = max(result, min(data))

print(result)