from math import *
def s():
    a=int(input('Введите сторону шестиугольника: '))
    p=(3*a)/2
    area=sqrt(p*((p-a)**3))
    print(area*6)
s()