s = input()
time = 0
d_dic = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'],
         6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}
for i in s:
    for k, v in d_dic.items():
        if i in v:
            time += int(k) + 1
print(time)

# num=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# s=input()
# time=0
# for i in s:
#     for j in num:
#         if i in j:
#             time+=num.index(j)+3
# print(time)