s = input()
lst = [-1] * 26
for i in range(len(s)):
    if lst[ord(s[i]) - 97] != -1:
        pass
    else:
        lst[ord(s[i]) - 97] = i
for i in lst:
    print(i, end=' ')

# s = list(input())
# c = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in c:
#     if i in s:
#         print(s.index(i), end =' ')
#     else:
#         print(-1, end=' ')
#
# s = input()
# for x in 'abcdefghijklmnopqrstuvwxyz':
#     print(s.find(x), end = ' ')

