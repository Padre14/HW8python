import view
import database

def main():
    while True:
        ask=view.user_input()
        if ask == 1:
            data=view.man()
            database.add_dat(data)
        elif ask == 2:
            name=view.serch_man_name()
            database.search_name(name)
        elif ask == 3:
            database.sort_db_name()
        elif ask == 4:
            database.sort_db_data()
        elif ask == 5:
            database.print_name()
        elif ask == 6:
            database.print_db()
        elif ask == 7:
            data_str=view.get_data_delete()
            lst_person=database.select_person(data_str)
            num=view.select_number()
            database.delete_person(lst_person[num-1])
        elif ask == 8:
            data_str=view.get_data_delete()
            lst_person=database.select_person(data_str)
            num=view.select_number()
            new_person=view.man()
            database.change_person(lst_person[num-1],new_person)       
        elif ask == 9: 
            break

main()          


