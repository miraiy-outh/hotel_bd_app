import tkinter as tk
from tkinter import messagebox
from tables.employee import *

ent_post = 0
ent_hotel = 0

# очистка полей ввода
def clear():
    ent_name.delete(0, last='end')
    ent_wd.delete(0, last='end')
    ent_salary.delete(0, last='end')
    ent_phoneNumber.delete(0, last='end')
    lbl2_post.delete(0, last='end')
    lbl2_hotel.delete(0, last='end')


# добавление сотрудника
def add_click():
    if get_name() != "error" and get_wd() != "error" and get_phone_number() != "error" and get_salary() != "error" and get_post() != "error" and get_hotel() != "error":
        employee = Employee(get_post(), get_hotel(), get_wd(), get_salary(), get_name(), get_phone_number())
        employee.insert_into_bd()
        messagebox.showinfo("ОК!", "Сотрудник добавлен")
        clear()
    else:
        messagebox.showinfo("Ошибка!", "Заполните все поля")


def get_name():
    result = ent_name.get()
    if result != "":
        return result
    else:
        return "error"


def get_wd():
    result = ent_wd.get()
    if result != "":
        return result
    else:
        return "error"

def get_salary():
    result = ent_salary.get()
    if result != "":
        return result
    else:
        return "error"

def get_phone_number():
    result = ent_phoneNumber.get()
    if result != "":
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

def add_ewindow():

    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для ввода сотрудника
    global ent_name
    lbl_name = tk.Label(master=frm_form, text="ФИО:")
    ent_name = tk.Entry(master=frm_form, width=50)
    lbl_name.grid(row=0, column=0, sticky="e")
    ent_name.grid(row=0, column=1)

    global ent_wd
    lbl_wd = tk.Label(master=frm_form, text="Количество раб. дней:")
    ent_wd = tk.Entry(master=frm_form, width=50)
    lbl_wd.grid(row=1, column=0, sticky="e")
    ent_wd.grid(row=1, column=1)

    global ent_salary
    lbl_salary = tk.Label(master=frm_form, text="Зарплата:")
    ent_salary = tk.Entry(master=frm_form, width=50)
    lbl_salary.grid(row=2, column=0, sticky="e")
    ent_salary.grid(row=2, column=1)

    global ent_phoneNumber
    lbl_phoneNumber = tk.Label(master=frm_form, text="Номер телефона:")
    ent_phoneNumber = tk.Entry(master=frm_form, width=50)
    lbl_phoneNumber.grid(row=3, column=0, sticky="e")
    ent_phoneNumber.grid(row=3, column=1)

    global lbl2_post
    lbl_post = tk.Label(master=frm_form, text="Исполняющая должность:")
    lbl2_post = tk.Entry(master=frm_form, width=50)
    lbl_post.grid(row=4, column=0, sticky="e")
    lbl2_post.grid(row=4, column=1, columnspan=1)

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
    lbl_hotel.grid(row=5, column=0, sticky="e")
    lbl2_hotel.grid(row=5, column=1, columnspan=1)

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
