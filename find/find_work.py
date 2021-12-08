from connect import *
import tkinter as tk
from tkinter import messagebox

# очистка полей ввода
def clear():
    ent_hotel.delete(0, last='end')
    ent_post.delete(0, last='end')


def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return ""


def add_post1():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0,'Администратор')
    lbl2_post = 1

def add_post2():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0,'Портье')
    lbl2_post = 2

def add_post3():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0,'Горничная')
    lbl2_post = 3

def add_post4():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0,'Повар')
    lbl2_post = 4

def add_post5():
    global ent_post
    global lbl2_post
    ent_post.delete(0, "end")
    ent_post.insert(0,'Слесарь/Электрик')
    lbl2_post = 5

def add_hotel1():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0,'Мечта')
    lbl2_hotel = 1

def add_hotel2():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0,'Лазурный')
    lbl2_hotel = 2

def add_hotel3():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0,'Россия')
    lbl2_hotel = 3

def add_hotel4():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0,'Урал')
    lbl2_hotel = 4

def add_hotel5():
    global ent_hotel
    global lbl2_hotel
    ent_hotel.delete(0, "end")
    ent_hotel.insert(0,'Южная')
    lbl2_hotel = 5

def change():
    global find_w
    if get_text(ent_hotel.get()) != '':
        find_w += f"hotelId='{lbl2_hotel}' AND "
    if get_text(ent_post.get()) != '':
        find_w += f"postId='{lbl2_post}' AND "
    find_w = find_w[0:len(find_w) - 4] + ";"

def post(tmp):
    f_post = f"""
            SELECT nameOfPost FROM
            post
            WHERE
            postId={tmp};
            """
    tmp = execute_read_query(connection, f_post)[0][0]
    return tmp

def hotel(tmp):
    f_hotel = f"""
                SELECT nameOfHotel FROM
                hotel
                WHERE
                hotelId={tmp};
                """
    tmp = execute_read_query(connection, f_hotel)[0][0]
    return tmp

def find_work():
    global find_w
    global text
    try:
        text.delete('1.0', 'end')
        find_w = "SELECT * FROM work WHERE "
        text.insert('1.0', 'ID Должность Описание Дедлайн Номер комнаты Отель\n')
        change()
        work_name = execute_read_query(connection, find_w)
        for i in work_name:
            tmp = [i[0], post(i[1]), i[2], str(i[3]), i[4], hotel(i[5])]
            text.insert('end', f'{tmp}\n')
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")
    return 0

def find_work_window():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    global ent_hotel
    global lbl_hotel
    global lbl2_hotel
    lbl_hotel = tk.Label(master=frm_form, text="Отель:")
    ent_hotel = tk.Entry(master=frm_form, width=50)
    lbl_hotel.grid(row=0, column=0, sticky="e")
    ent_hotel.grid(row=0, column=1)

    global ent_post
    global lbl_post
    global lbl2_post
    lbl_post = tk.Label(master=frm_form, text="Должность:")
    ent_post = tk.Entry(master=frm_form, width=50)
    lbl_post.grid(row=1, column=0, sticky="e")
    ent_post.grid(row=1, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

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

    global text
    text = tk.Text(width=100, height=15)
    text.pack()

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти", command=find_work)
    btn_submit.grid(row=4, column=0)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.grid(row=4, column=2)