from logger import add_phone_number, print_data, change_phone_number, delete_contact

def interface(file):
    print ("Добрый день! Вы попали на спец бот-справочник!\n 1 - Запись данных \n 2 - Вывод данных \n 3 - Изменение данных \n 4 - Удаление данных")
    command = int (input('Введите число '))

    while command != 1 and command != 2 and command != 3 and command !=4:
        print("Неправильный ввод")
        command = int (input('Введите число '))

#interface()

    if command == 1:
        add_phone_number(file)
    elif command == 2:
        print_data (file)
    elif command == 3:
        change_phone_number(file)
    elif command == 4:
        delete_contact(file)