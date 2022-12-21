# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


Quarter = int(input('Введите номер четверти: '))
if Quarter < 0 or  Quarter > 4:
    print('Введено неверное число')
elif Quarter == 1:
    print('X[0 inf] Y[0 inf]')
elif Quarter == 2:
    print('X[-inf 0] Y[0 inf]')
elif Quarter == 3:
    print('X[-inf 0] Y[-inf 0]')
else:
    print('X[0 inf] Y[-inf 0]')