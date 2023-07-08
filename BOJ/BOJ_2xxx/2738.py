n,m=map(int,input().split())
mat1=[]
mat2=[]
for i in range(n):
    mat1.append(list(map(int,input().split())))
for i in range(n):
    mat2.append(list(map(int,input().split())))
for m1,m2 in zip(mat1,mat2):
    for i in range(m):
        print(m1[i]+m2[i], end=' ')
    print()