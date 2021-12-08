import tkinter as tk
from tkinter import messagebox
from tables.client import *


# очистка полей ввода
def clear():
    ent_name.delete(0, last='end')
    ent_passport.delete(0, last='end')
    ent_phoneNumber.delete(0, last='end')


# добавление клиента
def add_click():
    if get_name() != "error" and get_passport() != "error" and get_phone_number() != "error":
        client = Client(get_name(), get_passport(), get_phone_number())
        client.insert_into_bd()
        messagebox.showinfo("ОК!", "Клиент добавлен")
        clear()
    else:
        messagebox.showinfo("Ошибка!", "Заполните все поля")


def get_name():
    result = ent_name.get()
    if result != "":
        return result
    else:
        return "error"


def get_passport():
    result = ent_passport.get()
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


def add_cwindow():

    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для ввода клиента
    global ent_name
    lbl_name = tk.Label(master=frm_form, text="ФИО:")
    ent_name = tk.Entry(master=frm_form, width=50)
    lbl_name.grid(row=0, column=0, sticky="e")
    ent_name.grid(row=0, column=1)

    global ent_passport
    lbl_passport = tk.Label(master=frm_form, text="Данные паспорта:")
    ent_passport = tk.Entry(master=frm_form, width=50)
    lbl_passport.grid(row=1, column=0, sticky="e")
    ent_passport.grid(row=1, column=1)

    global ent_phoneNumber
    lbl_phoneNumber = tk.Label(master=frm_form, text="Номер телефона:")
    ent_phoneNumber = tk.Entry(master=frm_form, width=50)
    lbl_phoneNumber.grid(row=2, column=0, sticky="e")
    ent_phoneNumber.grid(row=2, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Добавить", command=add_click)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
