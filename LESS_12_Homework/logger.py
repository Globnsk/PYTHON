from  data_create import name_data, surname_data, phone_data, address_data

def input_data ():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    return name, surname, phone, address
    # var = int(input(f"В каком формате записать данные\n\n"
    # f"Вариант 1: \n"
    # f"{name}\n{surname}\n{phone}\n{address}\n\n"
    # f"Вариант 2: \n"
    # f"{name};{surname};{phone};{address}\n"
    # f"Выберите вариант: "))
    # while var != 1 and var != 2:
    #     print("Неправильный ввод")
    #     var = int (input('Введите число '))
    
    # if var == 1:
    #     with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
    #         f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    # elif var == 2:
    #     with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
    #         f.write(f"{name};{surname};{phone};{address}\n\n")
    
def add_phone_number(file):
    info = ' '.join(input_data())
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{info}\n')

def print_data (file):
    # print ('Вывожу данные из Справочника:  \n')
    # with open('phonebook.csv', 'r', encoding='utf-8') as f:
    #     data_first = f.readlines()
    #     data_first_list = []
    #     j = 0
    #     for i in range(len(data_first)):
    #         if data_first[i] == '\n' or i == len(data_first) - 1:
    #             data_first_list.append(''.join(data_first[j:i+1]))
    #             j = i
    #     print (''.join(data_first_list))

    print ('Вывожу данные из Справочника:  \n')
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
    print(*data)

def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по имени\n2 - по фамилии\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n4 - адрес\n')
    if field == '1':
        number_to_change[0] = input('Введите имя: ')
    elif field == '2':
        number_to_change[1] = input('Введите фамилию: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    if field == '4':
        number_to_change[3] = input('Введите адрес: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


# change_data ():

#     pass


# def delete_data ():


#     pass


#print_data()