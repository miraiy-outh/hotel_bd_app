import tkinter as tk
from tkinter import messagebox
from tables.employee import *

lbl2_post = 0
lbl2_hotel = 0


# очистка полей ввода
def clear():
    ent_id.delete(0, last='end')
    ent_name.delete(0, last='end')
    ent_wd.delete(0, last='end')
    ent_salary.delete(0, last='end')
    ent_phoneNumber.delete(0, last='end')
    ent_post.delete(0, last='end')
    ent_hotel.delete(0, last='end')


def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return ""


# добавление атрибутов в запрос
def change():
    global alter_e
    if get_text(ent_name.get()) != '':
        alter_e += f"fullName='{ent_name.get()}', "
    if get_text(ent_wd.get()) != '':
        alter_e += f"workDays='{ent_wd.get()}', "
    if get_text(ent_salary.get()) != '':
        alter_e += f"salary='{ent_salary.get()}', "
    if get_text(ent_phoneNumber.get()) != '':
        alter_e += f"phoneNumber='{ent_phoneNumber.get()}', "
    if get_text(ent_post.get()) != '':
        alter_e += f"postId='{lbl2_post}', "
    if get_text(ent_hotel.get()) != '':
        alter_e += f"hotelId='{lbl2_hotel}', "
    alter_e = alter_e[0:len(alter_e) - 2] + f" WHERE employeeId={ent_id.get()};"


# изменение сотрудника
def alter_click():
    global alter_e
    if get_text(ent_id.get()) != "":
        alter_e = "UPDATE employee SET "
        change()
        execute_query(connection, alter_e)
        messagebox.showinfo("ОК!", "Сотрудник изменен")
        clear()
    else:
        messagebox.showinfo("Ошибка!", "Введите корректный ID сотрудника")


# выбор номера должности и отеля
def add_post1():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0, 'Администратор')
    lbl2_post = 1


def add_post2():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0, 'Портье')
    lbl2_post = 2


def add_post3():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0, 'Горничная')
    lbl2_post = 3


def add_post4():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0, 'Повар')
    lbl2_post = 4


def add_post5():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0, 'Слесарь/Электрик')
    lbl2_post = 5


def add_hotel1():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0, 'Мечта')
    lbl2_hotel = 1


def add_hotel2():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0, 'Лазурный')
    lbl2_hotel = 2


def add_hotel3():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0, 'Россия')
    lbl2_hotel = 3


def add_hotel4():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0, 'Урал')
    lbl2_hotel = 4


def add_hotel5():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0, 'Южная')
    lbl2_hotel = 5


def alter_ewindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для изменения сотрудника
    global ent_id
    lbl_id = tk.Label(master=frm_form, text="ID:")
    ent_id = tk.Entry(master=frm_form, width=50)
    lbl_id.grid(row=0, column=0, sticky="e")
    ent_id.grid(row=0, column=1)
    global ent_name
    lbl_name = tk.Label(master=frm_form, text="ФИО:")
    ent_name = tk.Entry(master=frm_form, width=50)
    lbl_name.grid(row=1, column=0, sticky="e")
    ent_name.grid(row=1, column=1)

    global ent_wd
    lbl_wd = tk.Label(master=frm_form, text="Количество раб. дней:")
    ent_wd = tk.Entry(master=frm_form, width=50)
    lbl_wd.grid(row=2, column=0, sticky="e")
    ent_wd.grid(row=2, column=1)

    global ent_salary
    lbl_salary = tk.Label(master=frm_form, text="Зарплата:")
    ent_salary = tk.Entry(master=frm_form, width=50)
    lbl_salary.grid(row=3, column=0, sticky="e")
    ent_salary.grid(row=3, column=1)

    global ent_phoneNumber
    lbl_phoneNumber = tk.Label(master=frm_form, text="Номер телефона:")
    ent_phoneNumber = tk.Entry(master=frm_form, width=50)
    lbl_phoneNumber.grid(row=4, column=0, sticky="e")
    ent_phoneNumber.grid(row=4, column=1)

    global ent_post
    lbl_post = tk.Label(master=frm_form, text="Исполняющая должность:")
    ent_post = tk.Entry(master=frm_form, width=50)
    lbl_post.grid(row=5, column=0, sticky="e")
    ent_post.grid(row=5, column=1, columnspan=1)

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

    global ent_hotel
    lbl_hotel = tk.Label(master=frm_form, text="Гостиница:")
    ent_hotel = tk.Entry(master=frm_form, width=50)
    lbl_hotel.grid(row=6, column=0, sticky="e")
    ent_hotel.grid(row=6, column=1, columnspan=1)

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
    btn_submit = tk.Button(master=frm_buttons, text="Изменить", command=alter_click)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
