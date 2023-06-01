import sys
sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    n=int(input())
    house=list(map(int,input().split()))
    result=0
    for i in range(2,len(house)-2):
        r1=house[i]-house[i+1]
        r2=house[i]-house[i+2]
        l1=house[i]-house[i-1]
        l2=house[i]-house[i-2]
        if r1>0 and r2>0 and l1>0 and l2>0:
            result+=min(r1,r2,l1,l2)
    print('#{} {}'.format(test_case,result))