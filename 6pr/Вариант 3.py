#1
n=int(input())
n=[int(input()) for i in range(n)]
s=0
for j in range(len(n)):
    if j%2!=0:
        s+=n[j]
print(n)
print(s)

#2
n=[int(input()) for i in range(8)]
for j in range(len(n)):
    if n[j]<15:
        n[j]=n[j]*2
print(n)