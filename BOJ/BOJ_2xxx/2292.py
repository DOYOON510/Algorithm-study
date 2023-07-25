n = int(input())
num = 1
cnt = 1
while num < n:
    num = num + (6 * cnt)
    cnt += 1
print(cnt)