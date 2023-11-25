s=input()
k=0
for i in s:
    if i=='а':
        s=s.replace('а', 'о')
        k+=1
print(s, k, len(s))