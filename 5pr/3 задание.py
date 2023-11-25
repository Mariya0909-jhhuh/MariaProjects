s=input()
b=s.count('.')
if '.' in s:
    s=s.replace('.', '')
print(s, b)