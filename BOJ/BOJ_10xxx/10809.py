s = input()
lst = [-1] * 26
for i in range(len(s)):
    if lst[ord(s[i]) - 97] != -1:
        pass
    else:
        lst[ord(s[i]) - 97] = i
for i in lst:
    print(i, end=' ')