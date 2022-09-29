fi=open('doitien.inp')
fo=open('doitien.out','w')
#Đọc file
n,s=list(map(int,fi.readline().split()))
c=[]
c.append(0)
ci=fi.read().split()
for x in ci:
    c.append(int(x))
#Xay dung bang phuong an
f=[[0]*(s+1) for i in range(n+1)]
for i in range(1,s+1):
    f[0][i]=float('inf')
for i in range(1,n+1):
    for j in range(1,s+1):
        f[i][j]=f[i-1][j]
        if j>=c[i]:
            f[i][j]=min(f[i-1][j],f[i][j-c[i]]+1)
print(f[n][s])
#Truy vet
i,j=n,s
k=[]
while i:
    while f[i][j]!=f[i-1][j]:
        k.append(i)
        j-=c[i]
    i-=1
print(k)
