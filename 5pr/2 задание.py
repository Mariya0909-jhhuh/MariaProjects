s=input()
a=s.count(":")
if ':' in s:
    s=s.replace(':', '%')
    print(s, a)