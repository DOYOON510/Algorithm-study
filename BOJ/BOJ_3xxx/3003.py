num=list(map(int,input().split()))
chess=[1,1,2,2,2,8]
for numi, chessi in zip(num,chess):
    print(chessi-numi, end=' ')