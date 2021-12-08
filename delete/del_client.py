from connect import *
import tkinter as tk
from tkinter import messagebox


# очистка полей ввода
def clear():
    ent_find_name.delete(0, last='end')
    ent_find_id.delete(0, last='end')

def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return "error"

def del_client_id():
    global client_id
    global ent_find_id
    try:
        del_client = f"""
                DELETE FROM
                client
                WHERE
                clientId={ent_find_id.get()};
                """
        client_id = execute_query(connection, del_client)
        messagebox.showinfo("ОК!", "Клиент удален")
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")

def del_client_name():
    global client_name
    global ent_find_name
    global text
    if ent_find_name.get() != "error":
        text.delete('1.0', 'end')
        del_client = f"""
                DELETE FROM
                client
                WHERE
                fullName LIKE '%{ent_find_name.get()}%';
                """
        client_name = execute_query(connection, del_client)
        messagebox.showinfo("ОК!", "Клиент удален")
    else:
        messagebox.showinfo("Ошибка!", "Заполните поле")
    return 0

def del_cwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для удаления клиента
    global ent_find_id
    lbl_find_id = tk.Label(master=frm_form, text="Введите ID клиента:")
    ent_find_id = tk.Entry(master=frm_form, width=50)
    lbl_find_id.grid(row=0, column=0, sticky="e")
    ent_find_id.grid(row=0, column=1)

    global ent_find_name
    lbl_find_name = tk.Label(master=frm_form, text="Введите ФИО клиента:")
    ent_find_name = tk.Entry(master=frm_form, width=50)
    lbl_find_name.grid(row=1, column=0, sticky="e")
    ent_find_name.grid(row=1, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Удалить по id", command=del_client_id)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Удалить по имени", command=del_client_name)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)