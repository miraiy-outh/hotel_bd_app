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


# нахождение по ID
def find_client_id():
    global client_id
    global ent_find_id
    global text
    try:
        text.delete('1.0', 'end')
        find_client = f"""
                SELECT * FROM
                client
                WHERE
                clientId={ent_find_id.get()};
                """
        text.insert('1.0', 'ID ФИО Паспортная информация Номер телефона\n')
        client_id = execute_read_query(connection, find_client)
        text.insert('2.0', client_id[0])
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")


# нахождение по имени
def find_client_name():
    global client_name
    global ent_find_name
    global text
    try:
        text.delete('1.0', 'end')
        find_client = f"""
                SELECT * FROM
                client
                WHERE
                fullName LIKE '%{ent_find_name.get()}%';
                """
        text.insert('1.0', 'ID            ФИО               Паспортная информация    Номер телефона\n')
        client_name = execute_read_query(connection, find_client)
        for i in client_name:
            text.insert('end', f'{i}\n')
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")
    return 0


def find_cwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для нахождения клиента
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

    global text
    text = tk.Text(width=100, height=15)
    text.pack()

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти по id", command=find_client_id)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти по имени", command=find_client_name)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
