n=int(input())
l=list(map(int,input().split()))
a,b=0,0
for i in set(l):
    if i%2==0:
        if l.count(i)%2==0:
            a+=1
        else:
            b+=1
    else:
        if l.count(i)%2==0:
            b+=1
        else:
            a+=1
if a>b:
    print("A",a-b)
elif b>a:
    print("B",b-a)
else:
    print("T 0")