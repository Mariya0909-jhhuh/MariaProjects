#1
l=int(input())
s=1
f=0
n=[int(input()) for i in range(l)]
for k in n:
    s*=k
    f+=k
print(s, f)

#2
l=int(input())
n=[int(input()) for i in range(l)]
s=0
for j in n:
    s+=j
    sa=s/l
for k in range(len(n)):
    if n[k]==0:
        n[k]=sa
print(n)