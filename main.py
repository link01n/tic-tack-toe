##################### ПРОЕКТ ИГРЫ КРЕСТИКИ-НОЛИКИ ######################################################################

##################### СОЗДАНИЕ ИГРОВОГО ПОЛЯ ###########################################################################

board = list(range(1,10)) #создаем переменную со списком, в котором 9 элементов

def draw_board(): #создаем функцию
    print ('-------------') #печатаем верхнюю границу игры
    for i in range(3): #в цикле перебираем весь список
#при значение i равном 0 выведем 1-ю строку и так от 0 до 2
#в квадратных скобках формула, для взятия значений из списка
#при проходе 1м циклом, i равен 0, прибавляем 1,2,3 и получаем 1,2,3
#при проходе 2м циклом, i равен 1, прибавляем 1,2,3 и получаем 4,5,6
#при проходе 3м циклом, i равен 2, прибавляем 1,2,3 и получаем 7,8,9
        print ('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print ('-------------') #выводим на экран подчёркивание после каждой строки
draw_board() #запускаем функцию, чтобы увидеть начальное игровое поле игры