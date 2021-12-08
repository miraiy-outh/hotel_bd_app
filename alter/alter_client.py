import tkinter as tk
from tkinter import messagebox
from tables.employee import *

lbl2_post = 0
lbl2_hotel = 0


# очистка полей ввода
def clear():
    ent_id.delete(0, last='end')
    ent_name.delete(0, last='end')
    ent_pswd.delete(0, last='end')
    ent_phoneNumber.delete(0, last='end')

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
    if get_text(ent_pswd.get()) != '':
        alter_e += f"passportInformation='{ent_pswd.get()}', "
    if get_text(ent_phoneNumber.get()) != '':
        alter_e += f"phoneNumber='{ent_phoneNumber.get()}', "
    alter_e = alter_e[0:len(alter_e) - 2] + f" WHERE clientId={ent_id.get()};"


# изменение сотрудника
def alter_click():
    global alter_e
    if get_text(ent_id.get()) != "":
        alter_e = "UPDATE client SET "
        change()
        print(alter_e)
        execute_query(connection, alter_e)
        messagebox.showinfo("ОК!", "Клиент изменен")
        clear()
    else:
        messagebox.showinfo("Ошибка!", "Введите корректный ID клиента")


def alter_cwindow():
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

    global ent_pswd
    lbl_wd = tk.Label(master=frm_form, text="Паспортная информация:")
    ent_pswd = tk.Entry(master=frm_form, width=50)
    lbl_wd.grid(row=2, column=0, sticky="e")
    ent_pswd.grid(row=2, column=1)

    global ent_phoneNumber
    lbl_phoneNumber = tk.Label(master=frm_form, text="Номер телефона:")
    ent_phoneNumber = tk.Entry(master=frm_form, width=50)
    lbl_phoneNumber.grid(row=4, column=0, sticky="e")
    ent_phoneNumber.grid(row=4, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Изменить", command=alter_click)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)