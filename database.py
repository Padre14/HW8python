def add_dat(data):
    with open("db.txt", "a") as file:
        file.write(data)
    print("Телефонная книга обновлена \n")
    

def search_name(name):
    with open("db.txt", "r") as file:
        data=file.readline()
        flag = False
        for i in data:
            if name in i:
                print(i)
                flag = True 
            if flag == False:
                print("Такого абонента не найдено \n")
                
        

def sort_db_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("db.txt", "w") as file:
        file.writelines(data) 
        
def sort_db_data():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key=lambda x: x[4])
    with open("db.txt", "w") as file:
        file.writelines(data) 
    
def print_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i.split(";")[0])
            
def print_db():
    with open("db.txt", "r") as file:
        print(file.read())

def find_person(data_str):
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            if data_str in i:
                print(i)


def select_person(data_str):
    lst_person=[]
    count=1
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            if data_str in i:
                print(f"{count}) {i}")
                count+=1
                lst_person.append(i)
    return lst_person

def delete_person(data_str):
    full_lst=[]
    with open("db.txt", "r") as file:
        full_lst = file.readlines()
    with open("db.txt", "w") as file:
        for i in full_lst:
            if data_str == i:
                continue
            file.write(i)
    print("запись удалена")

def change_person(old_str, new_str):
    with open("db.txt", "r") as file:
        full_lst = file.readlines()
    with open("db.txt", "w") as file:
        for i in full_lst:
            if i == old_str:
                file.write(new_str)
                continue
            file.write(i)
    print("запись изменена")
