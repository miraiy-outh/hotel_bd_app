from connect import *
import tkinter as tk
from tkinter import messagebox


# очистка полей ввода
def clear():
    ent_find_hname.delete(0, last='end')
    ent_find_hid.delete(0, last='end')

def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return "error"

def find_hotel_id():
    global hotel_id
    global ent_find_hid
    global htext
    try:
        htext.delete('1.0', 'end')
        find_hotel = f"""
                SELECT * FROM
                hotel
                WHERE
                hotelId={ent_find_hid.get()};
                """
        htext.insert('1.0', 'ID Название Адрес Номер телефона\n')
        hotel_id = execute_read_query(connection, find_hotel)
        htext.insert('2.0', hotel_id[0])
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")

def find_hotel_name():
    global client_name
    global ent_find_hname
    global htext
    try:
        htext.delete('1.0', 'end')
        find_hotel = f"""
                SELECT * FROM
                hotel
                WHERE
                nameOfHotel LIKE '%{ent_find_hname.get()}%';
                """
        htext.insert('1.0', 'ID Название Адрес Номер телефона\n')
        client_name = execute_read_query(connection, find_hotel)
        for i in client_name:
            htext.insert('end', f'{i}\n')
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")
    return 0

def find_hwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для поиска отеля
    global ent_find_hid
    lbl_find_hid = tk.Label(master=frm_form, text="Введите ID отеля:")
    ent_find_hid = tk.Entry(master=frm_form, width=50)
    lbl_find_hid.grid(row=0, column=0, sticky="e")
    ent_find_hid.grid(row=0, column=1)

    global ent_find_hname
    lbl_find_hname = tk.Label(master=frm_form, text="Введите название отеля:")
    ent_find_hname = tk.Entry(master=frm_form, width=50)
    lbl_find_hname.grid(row=1, column=0, sticky="e")
    ent_find_hname.grid(row=1, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    global htext
    htext = tk.Text(width=100, height=15)
    htext.pack()

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти по id", command=find_hotel_id)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти по названию", command=find_hotel_name)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)