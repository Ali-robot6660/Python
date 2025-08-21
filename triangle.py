# объявление функции
def draw_triangle():
    probel = 7
    for i in range(1,16,2):
        #for j in range(8):
        print( ' ' * probel, '*' * i, sep='') # вывод строки с пробелами и звёздочками
        probel -= 1

# основная программа
draw_triangle()  # вызов функции