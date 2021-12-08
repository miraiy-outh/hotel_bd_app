import tkinter as tk
from dict_auth import *
from tkinter import messagebox
from menu.op_menu import *
from menu.adm_menu import *


def search_d(login, pswd, role):
    for i in range(0, len(user_dict[role])):
        tmp = 0
        if user_dict[role][i][0] == login and user_dict[role][i][1] == pswd:
            tmp = 1
            break
    return tmp


def login_click_op():
    login = ent_un.get()
    password = ent_pw.get()

    if search_d(login, password, 'operator') == 1:
        login_window.destroy()
        open_menu()
    else:
        messagebox.showinfo("Ошибка!", "Неверный логин или пароль")


def login_click_admin():
    login = ent_un.get()
    password = ent_pw.get()

    if search_d(login, password, 'admin') == 1:
        login_window.destroy()
        open_adm_menu()
    else:
        messagebox.showinfo("Ошибка!", "Неверный логин или пароль")


def login():
    global login_window
    login_window = tk.Tk()
    login_window.title('Авторизация')
    login_window.geometry('600x100')
    login_window.resizable(False, False)
    frm_login = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_login.pack(side=tk.TOP)

    # поля для ввода логина и пароля
    global ent_un
    lbl_un = tk.Label(master=frm_login, text="Логин:")
    ent_un = tk.Entry(master=frm_login, width=80)
    lbl_un.grid(row=0, column=0, sticky="e")
    ent_un.grid(row=0, column=1)

    global ent_pw
    lbl_pw = tk.Label(master=frm_login, text="Пароль:")
    ent_pw = tk.Entry(master=frm_login, width=80)
    lbl_pw.grid(row=1, column=0, sticky="e")
    ent_pw.grid(row=1, column=1)

    # кнопка отправки формы
    login_buttons = tk.Frame()
    login_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    op_btn = tk.Button(master=login_buttons, text="Войти как оператор", command=login_click_op)
    op_btn.pack(side=tk.LEFT, padx=10, ipadx=10)
    adm_btn = tk.Button(master=login_buttons, text="Войти как администратор", command=login_click_admin)
    adm_btn.pack(side=tk.RIGHT, padx=10, ipadx=10)

    login_window.mainloop()
