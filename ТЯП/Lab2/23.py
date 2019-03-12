N = int(input('Введите кол-во элементов списка(больше 10): '))
sp = []
if N > 10:
    for i in range (0, N):
        sp.append(int(input('Введите ' + str(i+1) +' элемент списка: ')))
    print(sp)
    for i in range (5):
        sp.append(int(input('Введите новый элемент списка ' + str(i+1) + ': ')))
    print(len(sp))
    sp=[x for x in sp if x % 2 == 1]
    print(sp)
else:
    print('Вводимое число должно быть больше 10')
