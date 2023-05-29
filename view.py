def user_input():
    ask=int(input("Выберите ниже: \n 1 - записать пользователя \n 2 - поиск по имени \n 3 - сортировать справочник  по имени \n 4 - сортировать по дате рождения \n 5 - вывести только имена \n 6 - вывод справочника \n 7 - удалить контакт \n 8 - изменить контакт \n 9 - выйти"))
    return ask
    
def man():
    data = list()
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    father = input("Введите отчество: ")
    date = input("Введите дату рождения: ")
    telephone = input("Введите номер телефона: ")
    data= name + "; "+ family +"; "+ father + "; " + date +"; "+ telephone +"; " + "\n"
    return data


def serch_man_name():
    str_search= input("Введите имя для поиска")
    return str_search

def get_data_delete():
    data= input("введите данные абонента, которые хотите удалить")
    return data

def select_number():
    num= int(input("выберете строчку для изменения"))
    return num
    

# d=man()
# print(d)