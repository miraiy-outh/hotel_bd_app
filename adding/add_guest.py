import tkinter as tk
from tkinter import messagebox
from tables.guest import *


# очистка полей ввода
def clear():
    ent_card.delete(0, last='end')
    ent_room.delete(0, last='end')
    ent_bill.delete(0, last='end')
    ent_atime1.delete(0, last='end')
    ent_dtime1.delete(0, last='end')
    ent_atime2.delete(0, last='end')
    ent_dtime2.delete(0, last='end')
    ent_atime3.delete(0, last='end')
    ent_dtime3.delete(0, last='end')
    ent_id.delete(0, last='end')


def find_client():
    tmp = 0
    find = "SELECT clientId FROM client;"
    find2 = "SELECT clientId FROM guest;"
    array = execute_read_query(connection, find)
    array2 = execute_read_query(connection, find2)
    for i in range(0, len(array)):
        if int(array[i][0]) == int(get_id()):
            tmp = 1
    for i in range(0, len(array2)):
        if int(array2[i][0]) == int(get_id()):
            tmp = 2
    return tmp


# добавление постояльца
def add_click():
    if get_card() != "error" and get_room() != "error" and get_bill() != "error" and get_atime() != "error" and get_dtime() != "error":
        if find_client() == 1:
            guest = Guest(get_id(), get_card(), get_room(), get_bill(), get_atime(), get_dtime())
            guest.insert_into_bd()
            messagebox.showinfo("ОК!", "Постоялец добавлен")
            clear()
        else:
            if find_client() == 0:
                messagebox.showinfo("Ошибка!", "Такого клиента не существует")
                ent_id.delete(0, last='end')
            else:
                messagebox.showinfo("Ошибка!", "Постоялец уже существует")
                ent_id.delete(0, last='end')
    else:
        messagebox.showinfo("Ошибка!", "Заполните все поля")


def get_id():
    result = ent_id.get()
    if result != "":
        return result
    else:
        return "error"


def get_card():
    result = ent_card.get()
    if result != "":
        return result
    else:
        return "error"


def get_room():
    result = ent_room.get()
    if result != "":
        return result
    else:
        return "error"


def get_bill():
    result = ent_bill.get()
    if result != "":
        return result
    else:
        return "error"


def get_atime():
    result = ent_atime1.get() + "." + ent_atime2.get() + "." + ent_atime3.get()
    if result != "..":
        return result
    else:
        return "error"


def get_dtime():
    result = ent_dtime1.get() + "." + ent_dtime2.get() + "." + ent_dtime3.get()
    if result != "..":
        return result
    else:
        return "error"


def add_gwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для ввода постояльца
    global ent_id
    lbl_id = tk.Label(master=frm_form, text="ID клиента:")
    ent_id = tk.Entry(master=frm_form, width=50)
    lbl_id.grid(row=0, column=0, sticky="e")
    ent_id.grid(row=0, column=1, columnspan=3)

    global ent_card
    lbl_card = tk.Label(master=frm_form, text="Данные карты:")
    ent_card = tk.Entry(master=frm_form, width=50)
    lbl_card.grid(row=1, column=0, sticky="e")
    ent_card.grid(row=1, column=1, columnspan=3)

    global ent_room
    lbl_room = tk.Label(master=frm_form, text="Номер комнаты:")
    ent_room = tk.Entry(master=frm_form, width=50)
    lbl_room.grid(row=2, column=0, sticky="e")
    ent_room.grid(row=2, column=1, columnspan=3)

    global ent_bill
    lbl_bill = tk.Label(master=frm_form, text="Счет:")
    ent_bill = tk.Entry(master=frm_form, width=50)
    lbl_bill.grid(row=3, column=0, sticky="e")
    ent_bill.grid(row=3, column=1, columnspan=3)

    global ent_atime1
    global ent_atime2
    global ent_atime3
    lbl_atime = tk.Label(master=frm_form, text="Время прибытия:")
    ent_atime1 = tk.Entry(master=frm_form, width=2)
    ent_atime2 = tk.Entry(master=frm_form, width=2)
    ent_atime3 = tk.Entry(master=frm_form, width=4)
    lbl_atime.grid(row=4, column=0, sticky="e")
    ent_atime1.grid(row=4, column=1, sticky="e")
    ent_atime2.grid(row=4, column=2, sticky="e")
    ent_atime3.grid(row=4, column=3, sticky="e")

    global ent_dtime1
    global ent_dtime2
    global ent_dtime3
    lbl_dtime = tk.Label(master=frm_form, text="Время отбытия:")
    ent_dtime1 = tk.Entry(master=frm_form, width=2)
    ent_dtime2 = tk.Entry(master=frm_form, width=2)
    ent_dtime3 = tk.Entry(master=frm_form, width=4)
    lbl_dtime.grid(row=5, column=0, sticky="e")
    ent_dtime1.grid(row=5, column=1, sticky="e")
    ent_dtime2.grid(row=5, column=2, sticky="e")
    ent_dtime3.grid(row=5, column=3, sticky="e")

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Добавить", command=add_click)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
