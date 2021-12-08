from tkinter import Tk, Menu
from adding.add_employee import *
from find.find_client import *
from find.find_employee import *
from find.find_guest import *
from delete.del_client import *
from delete.del_employee import *
from alter.alter_employee import *

def clear_frame():
    for widget in op.winfo_children():
        if widget != adm_mainmenu:
            widget.destroy()


def add_empl():
    clear_frame()
    add_ewindow()


def find_clnt():
    clear_frame()
    find_cwindow()


def find_gst():
    clear_frame()
    find_gwindow()


def find_empl():
    clear_frame()
    find_ewindow()


def del_clnt():
    clear_frame()
    del_cwindow()


def del_empl():
    clear_frame()
    del_ewindow()


def alt_empl():
    clear_frame()
    alter_ewindow()

def reg_empl():
    clear_frame()
    reg()

def open_adm_menu():
    global op
    op = Tk()
    op.title('Меню администратора')
    op.geometry('800x300')
    op.resizable(False, False)
    global adm_mainmenu
    adm_mainmenu = Menu(op)
    op.config(menu=adm_mainmenu)

    addmenu = Menu(adm_mainmenu, tearoff=0)
    addmenu.add_command(label="Сотрудника", command=add_empl)

    formatmenu = Menu(adm_mainmenu, tearoff=0)
    formatmenu.add_command(label="Информацию сотрудника", command=alt_empl)

    findmenu = Menu(adm_mainmenu, tearoff=0)
    findmenu.add_command(label="Клиента", command=find_clnt)
    findmenu.add_command(label="Сотрудника", command=find_empl)

    deletemenu = Menu(adm_mainmenu, tearoff=0)
    deletemenu.add_command(label="Клиента", command=del_clnt)
    deletemenu.add_command(label="Сотрудника", command=del_empl)

    adm_mainmenu.add_cascade(label='Добавить', menu=addmenu)
    adm_mainmenu.add_cascade(label='Изменить', menu=formatmenu)
    adm_mainmenu.add_cascade(label='Найти/Вывести', menu=findmenu)
    adm_mainmenu.add_cascade(label='Удалить', menu=deletemenu)

    op.mainloop()
