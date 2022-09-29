fi=open('cuochop.inp')
fo = open('cuochop.out', 'w')
n=int(fi.readline())
s=[]
e=[]
v=[]
for i in range(n):
    si,ei,vi=list(map(int,fi.readline().split()))
    s.append(si)
    e.append(ei)
    v.append(vi)
s[:0]=[0] #chen dau list c ptu 0
e[:0]=[0] #chen dau list c ptu 0
v[:0]=[0]
#tao list luu thu tu
ee=e.copy()
#Xep cuoc hop gio ket thuc tang dan
for i in range(1,n+1):
    for j in range(1,i):
        if e[i]<=e[j]:
            tam,tam2,t3=e[i],s[i],v[i]
            e[i],s[i],v[i]=e[j],s[j],v[j]
            e[j],s[j],v[j]=tam,tam2,t3
#Xay dung bang phuong an
f=[0]*(n+1)
t=[0]*(n+1)
f[1]=1
for i in range(1,n+1):
    f[i]=v[i]
    for j in range(1,i):
        if s[i]>=e[j] and f[i]<f[j]+v[i]:
            f[i]=f[j]+v[i]
            t[i]=j
print(max(f))
#truy vet
k=[]
csm=f.index(max(f))
while t[csm]:
    k.append(e[csm])
    csm=t[csm]
k.append(e[csm])
k=sorted(k)
for i in ee:
    if i in k:
        print(ee.index(i))
print(k)