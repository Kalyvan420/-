import random
num=random.randint(0,100)
prog=False
while prog==False:
    a=int(input('Введите число:'))
    if a==num:
        prog=True
        print('Вы угадали число!')
    elif a > num:
        print('Ваше число больше загаданного!')
    else:
        print('Ваше число меньше загаданного!')