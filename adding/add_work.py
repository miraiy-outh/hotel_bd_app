import tkinter as tk
from tkinter import messagebox
from tables.work import *

ent_post = 0
ent_hotel = 0

# очистка полей ввода
def clear():
    text.delete(0, last='end')
    ent_room.delete(0, last='end')
    lbl2_post.delete(0, last='end')
    ent_time1.delete(0, last='end')
    ent_time2.delete(0, last='end')
    ent_time3.delete(0, last='end')
    lbl2_hotel.delete(0, last='end')

# добавление работы
def add_click():
    print(ent_post, ent_hotel)
    if get_descr() != "error" and get_room() != "error" and get_time() != "error" and get_post() != "error" and get_hotel() != "error":
        work = Work(get_post(), get_descr(), get_time(), get_room(), get_hotel())
        work.insert_into_bd()
        messagebox.showinfo("ОК!", "Работа добавлена")
        clear()
    else:
        messagebox.showinfo("Ошибка!", "Заполните все поля")


def get_descr():
    result = text.get()
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


def get_time():
    result = ent_time1.get() + "." + ent_time2.get() + "." + ent_time3.get()
    if result != "..":
        return result
    else:
        return "error"

def get_post():
    if ent_post != 0:
        return ent_post
    else:
        return "error"

def get_hotel():
    if ent_hotel != 0:
        return ent_hotel
    else:
        return "error"

def add_post1():
    global ent_post
    lbl2_post.delete(0, "end")
    lbl2_post.insert(0,'Администратор')
    ent_post = 1

def add_post2():
    global ent_post
    lbl2_post.delete(0, "end")
    lbl2_post.insert(0,'Портье')
    ent_post = 2

def add_post3():
    global ent_post
    lbl2_post.delete(0, "end")
    lbl2_post.insert(0,'Горничная')
    ent_post = 3

def add_post4():
    global ent_post
    lbl2_post.delete(0, "end")
    lbl2_post.insert(0,'Повар')
    ent_post = 4

def add_post5():
    global ent_post
    lbl2_post.delete(0, "end")
    lbl2_post.insert(0,'Слесарь/Электрик')
    ent_post = 5

def add_hotel1():
    global ent_hotel
    lbl2_hotel.delete(0, "end")
    lbl2_hotel.insert(0,'Мечта')
    ent_hotel = 1

def add_hotel2():
    global ent_hotel
    lbl2_hotel.delete(0, "end")
    lbl2_hotel.insert(0,'Лазурный')
    ent_hotel = 2

def add_hotel3():
    global ent_hotel
    lbl2_hotel.delete(0, "end")
    lbl2_hotel.insert(0,'Россия')
    ent_hotel = 3

def add_hotel4():
    global ent_hotel
    lbl2_hotel.delete(0, "end")
    lbl2_hotel.insert(0,'Урал')
    ent_hotel = 4

def add_hotel5():
    global ent_hotel
    lbl2_hotel.delete(0, "end")
    lbl2_hotel.insert(0,'Южная')
    ent_hotel = 5

def add_work_window():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для ввода работ
    global text
    lbl_descr = tk.Label(master=frm_form, text="Описание работы:")
    text = tk.Entry(master=frm_form, width=50)
    lbl_descr.grid(row=0, column=0, sticky="e")
    text.grid(row=0, column=1, columnspan=3)

    global ent_room
    lbl_room = tk.Label(master=frm_form, text="Номер комнаты:")
    ent_room = tk.Entry(master=frm_form, width=50)
    lbl_room.grid(row=1, column=0, sticky="e")
    ent_room.grid(row=1, column=1, columnspan=3)

    global ent_time1
    global ent_time2
    global ent_time3
    lbl_time = tk.Label(master=frm_form, text="Дедлайн:")
    ent_time1 = tk.Entry(master=frm_form, width=2)
    ent_time2 = tk.Entry(master=frm_form, width=2)
    ent_time3 = tk.Entry(master=frm_form, width=4)
    lbl_time.grid(row=2, column=0, sticky="w")
    ent_time1.grid(row=2, column=1, sticky="e")
    ent_time2.grid(row=2, column=2, sticky="e")
    ent_time3.grid(row=2, column=3, sticky="e")

    global lbl2_post
    lbl_post = tk.Label(master=frm_form, text="Исполняющая должность:")
    lbl2_post = tk.Entry(master=frm_form, width=50)
    lbl_post.grid(row=3, column=0, sticky="e")
    lbl2_post.grid(row=3, column=1, columnspan=1)

    frm_post = tk.Frame()
    frm_post.pack(fill=tk.Y, ipadx=5, ipady=5)
    btn_post1 = tk.Button(master=frm_post, text="Администратор", command=add_post1)
    btn_post1.pack(side=tk.LEFT, padx=10, ipadx=10)
    btn_post2 = tk.Button(master=frm_post, text="Портье", command=add_post2)
    btn_post2.pack(side=tk.LEFT, padx=10, ipadx=10)
    btn_post3 = tk.Button(master=frm_post, text="Горничная", command=add_post3)
    btn_post3.pack(side=tk.LEFT, padx=10, ipadx=10)
    btn_post4 = tk.Button(master=frm_post, text="Повар", command=add_post4)
    btn_post4.pack(side=tk.LEFT, padx=10, ipadx=10)
    btn_post5 = tk.Button(master=frm_post, text="Слесарь/Электрик", command=add_post5)
    btn_post5.pack(side=tk.LEFT, padx=10, ipadx=10)

    global lbl2_hotel
    lbl_hotel = tk.Label(master=frm_form, text="Гостиница:")
    lbl2_hotel = tk.Entry(master=frm_form, width=50)
    lbl_hotel.grid(row=4, column=0, sticky="e")
    lbl2_hotel.grid(row=4, column=1, columnspan=1)

    frm_hotel = tk.Frame()
    frm_hotel.pack(fill=tk.Y, ipadx=10, ipady=10)
    btn_hotel1 = tk.Button(master=frm_hotel, text="Мечта", command=add_hotel1)
    btn_hotel1.pack(side=tk.RIGHT, padx=10, ipadx=10)
    btn_hotel2 = tk.Button(master=frm_hotel, text="Лазурный", command=add_hotel2)
    btn_hotel2.pack(side=tk.RIGHT, padx=10, ipadx=10)
    btn_hotel3 = tk.Button(master=frm_hotel, text="Россия", command=add_hotel3)
    btn_hotel3.pack(side=tk.RIGHT, padx=10, ipadx=10)
    btn_hotel4 = tk.Button(master=frm_hotel, text="Урал", command=add_hotel4)
    btn_hotel4.pack(side=tk.RIGHT, padx=10, ipadx=10)
    btn_hotel5 = tk.Button(master=frm_hotel, text="Южная", command=add_hotel5)
    btn_hotel5.pack(side=tk.RIGHT, padx=10, ipadx=10)


    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Добавить", command=add_click)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
