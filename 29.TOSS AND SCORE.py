s=input()
scr=0
for i in range(len(s)):
    if s[i]=="H":
        scr+=2
        if s[i-2:i+1]=="HHH":
            break
    elif s[i]=="T":
        scr-=1
print(scr)