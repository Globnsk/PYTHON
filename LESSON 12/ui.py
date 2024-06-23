

def intrface():
    print ("Добрый день! Вы попали на спец бот-справочник!\n 1 - Запись данных \n  2 - Вывод данных")
    command = int (input('Введите число'))

    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int (input('Введите число '))

interface()