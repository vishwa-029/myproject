s=input()
a="abcdefghijklmnopqrstuvwxyz"
d=""
for i in a:
    if i not in s:
        d+=i
print(d)