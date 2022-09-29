fi=open('balo2.inp')
fo=open('balo.out','w')
#Đọc file
n,b=list(map(int,fi.readline().split()))
print(n,b)
c=[]
w=[]
c.append(0)
w.append(0)
for i in range(1,n+1):
    ci, wi = list(map(int, fi.readline().split()))
    c.append(ci)
    w.append(wi)
#Khởi tạo list kq là bảng kết quả
kq=[ [0]*(b+1) for i in range(n+1)]
#Công thức QHĐ đẻ xây dựng bảng kết quả
for i in range(1,n+1):
    for j in range(1,b+1):
        kq[i][j]=kq[i-1][j]
        if j>=w[i]:
            kq[i][j]=max(kq[i-1][j],kq[i][j-w[i]]+c[i])
fo.write(f'{kq[n][b]} \n')
#Truy vết từ cuối bảng kết qua
i=n
j=b
s=[]
while i:
    if kq[i][j]!=kq[i-1][j]:
        s.append(i)
        j=j-w[i]
    i-=1
fo.write(f'{s}')
