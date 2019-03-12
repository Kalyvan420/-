a=int(input('Введите число a: '))
b=int(input('Введите число b: '))
c=int(input('Введите число c: '))
d=int(input('Введите число d: '))
f=int(input('Введите число f: '))
if a!=0:
    print(abs(a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213)))
else:
    print('Число а не может ровнятся нулю')
