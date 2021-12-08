from connect import *
import tkinter as tk
from tkinter import messagebox


# очистка полей ввода
def clear():
    ent_find_id.delete(0, last='end')


def del_guest_id():
    global guest_id
    global ent_find_id
    try:
        del_guest = f"""
                DELETE FROM
                guest
                WHERE
                clientId={ent_find_id.get()};
                """
        guest_id = execute_query(connection, del_guest)
        messagebox.showinfo("ОК!", "Постоялец удален")
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")


def del_gwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для удаления постояльца
    global ent_find_id
    lbl_find_id = tk.Label(master=frm_form, text="Введите ID клиента:")
    ent_find_id = tk.Entry(master=frm_form, width=50)
    lbl_find_id.grid(row=0, column=0, sticky="e")
    ent_find_id.grid(row=0, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Удалить", command=del_guest_id)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
