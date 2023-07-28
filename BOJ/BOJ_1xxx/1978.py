n = int(input())
num_lst = list(map(int, input().split()))
result = 0
for i in num_lst:
    div = 0
    if i == 1:
        pass
    else:
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div == 2:
            result += 1
print(result)

'''
n = int(input())
num_lst = list(map(int, input().split()))
result = 0

for x in num_lst:
  if x <= 1: continue
  for j in range(2, int(x ** 1/2)+1):
    if x % j == 0: break
  else:
    result += 1

print(result)
'''