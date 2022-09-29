fi=open('daycon.inp')
fo = open('daycon.out', 'w')
n=int(fi.readline())
c=list(map(int,fi.read().split()))
c[:0]=[0] #chen dau list c ptu 0
#Xay dung bang phuong an
f=[0]*(n+1)
t=[0]*(n+1)
f[1]=1
for i in range(1,n+1):
    for j in range(1,i):
        if c[i]>c[j] and f[i]<f[j]+1:
            f[i]=f[j]+1
            t[i]=j
print(max(f))
#truy vet
k=[]
csm=f.index(max(f))
while t[csm]:
    k.append(c[csm])
    csm=t[csm]
k.append(c[csm])
k=sorted(k)
print(k)