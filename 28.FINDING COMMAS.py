n=int(input())
d=len(str(n))
t=0
for i in range(1,d):
    c=(i-1)//3
    num=9*(10**(i-1))
    t+=c*num
c=(d-1)//3
num=(n-(10**(d-1)))+1
t+=c*num
print(t)