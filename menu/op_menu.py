from tkinter import Tk, Menu
from adding.add_client import *
from adding.add_guest import *
from adding.add_work import *
from find.find_client import *
from find.find_employee import *
from find.find_guest import *
from find.find_hotel import *
from find.find_room import *
from find.find_work import *
from delete.del_guest import *
from delete.del_work import *
from alter.alter_client import *
from alter.alter_room import *


def clear_frame():
    for widget in op.winfo_children():
        if widget != mainmenu:
            widget.destroy()


def add_clnt():
    clear_frame()
    add_cwindow()


def add_gst():
    clear_frame()
    add_gwindow()


def add_wrk():
    clear_frame()
    add_work_window()


def find_clnt():
    clear_frame()
    find_cwindow()


def find_gst():
    clear_frame()
    find_gwindow()


def find_emp():
    clear_frame()
    find_ewindow()


def find_htl():
    clear_frame()
    find_hwindow()


def find_rm():
    clear_frame()
    find_rwindow()


def find_wrk():
    clear_frame()
    find_work_window()


def del_gst():
    clear_frame()
    del_gwindow()


def del_wrk():
    clear_frame()
    del_work_window()


def alt_clnt():
    clear_frame()
    alter_cwindow()

def alt_room():
    clear_frame()
    alter_rwindow()


def open_menu():
    global op
    op = Tk()
    op.title('Меню оператора')
    op.geometry('800x400')
    op.resizable(False, False)
    global mainmenu
    mainmenu = Menu(op)
    op.config(menu=mainmenu)

    addmenu = Menu(mainmenu, tearoff=0)
    addmenu.add_command(label="Клиента", command=add_clnt)
    addmenu.add_command(label="Постояльца", command=add_gst)
    addmenu.add_command(label="Работу", command=add_wrk)

    formatmenu = Menu(mainmenu, tearoff=0)
    formatmenu.add_command(label="Информацию клиента", command=alt_clnt)
    formatmenu.add_command(label="Состояние комнаты", command=alt_room)

    findmenu = Menu(mainmenu, tearoff=0)
    findmenu.add_command(label="Клиента", command=find_clnt)
    findmenu.add_command(label="Постояльца", command=find_gst)
    findmenu.add_command(label="Сотрудника", command=find_emp)
    findmenu.add_command(label="Гостиницу", command=find_htl)
    findmenu.add_command(label="Комнату", command=find_rm)
    findmenu.add_command(label="Работу", command=find_wrk)

    delmenu = Menu(mainmenu, tearoff=0)
    delmenu.add_command(label="Постояльца", command=del_gst)
    delmenu.add_command(label="Работу", command=del_wrk)

    mainmenu.add_cascade(label='Добавить', menu=addmenu)
    mainmenu.add_cascade(label='Изменить', menu=formatmenu)
    mainmenu.add_cascade(label='Найти/Вывести', menu=findmenu)
    mainmenu.add_cascade(label='Удалить', menu=delmenu)

    op.mainloop()
