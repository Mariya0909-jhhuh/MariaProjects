x=int(input('Введите натуральное число:'))
n=int(input('Введите число факториал которого хотите найти:'))
def factrorial(n):
    if n==0:
        return 1
    return factrorial(n-1)*n
print((x**n)/factrorial(n))
