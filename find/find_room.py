from connect import *
import tkinter as tk
from tkinter import messagebox


# очистка полей ввода
def clear():
    ent_find_class.delete(0, last='end')
    ent_find_rid.delete(0, last='end')
    ent_find_free.delete(0, last='end')
    ent_find_repair.delete(0, last='end')
    ent_find_clean.delete(0, last='end')


def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return ""


#заполнение полей
def free():
    global ent_find_free
    ent_find_free.delete(0, last='end')
    ent_find_free.insert(0, 'да')


def notfree():
    global ent_find_free
    ent_find_free.delete(0, last='end')
    ent_find_free.insert(0, 'нет')


def clean():
    global ent_find_clean
    ent_find_clean.delete(0, last='end')
    ent_find_clean.insert(0, 'да')


def notclean():
    global ent_find_clean
    ent_find_clean.delete(0, last='end')
    ent_find_clean.insert(0, 'нет')


def repair():
    global ent_find_repair
    ent_find_repair.delete(0, last='end')
    ent_find_repair.insert(0, 'да')


def notrepair():
    global ent_find_repair
    ent_find_repair.delete(0, last='end')
    ent_find_repair.insert(0, 'нет')


def econom():
    global ent_find_class
    ent_find_class.delete(0, last='end')
    ent_find_class.insert(0, 'эконом')


def comfort():
    global ent_find_class
    ent_find_class.delete(0, last='end')
    ent_find_class.insert(0, 'комфорт')


def lux():
    global ent_find_class
    ent_find_class.delete(0, last='end')
    ent_find_class.insert(0, 'люкс')


# добавление атрибутов в запрос
def change():
    global find_r
    if get_text(ent_find_free.get()) != '':
        if get_text(ent_find_free.get()) == 'да':
            find_r += "isFree=1 AND "
        if get_text(ent_find_free.get()) == 'нет':
            find_r += "isFree=0 AND "
    if get_text(ent_find_clean.get()) != '':
        if get_text(ent_find_clean.get()) == 'да':
            find_r += "isCleaned=1 AND "
        if get_text(ent_find_clean.get()) == 'нет':
            find_r += "isCleaned=0 AND "
    if get_text(ent_find_repair.get()) != '':
        if get_text(ent_find_repair.get()) == 'да':
            find_r += "needToRepair=1 AND "
        if get_text(ent_find_repair.get()) == 'нет':
            find_r += "needToRepair=0 AND "
    if get_text(ent_find_class.get()) != '':
        find_r += f"classOfRoom='{get_text(ent_find_class.get())}' AND "
    find_r = find_r[0:len(find_r) - 4] + ";"


def find_room():
    global find_r
    global rtext
    try:
        rtext.delete('1.0', 'end')
        find_r = "SELECT numberOfRoom, hotelId FROM room WHERE "
        rtext.insert('1.0', 'Номер Отель\n')
        change()
        room_name = execute_read_query(connection, find_r)
        for i in room_name:
            rtext.insert('end', f'{i}\n')
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")
    return 0


def find_rwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для поиска комнаты
    global ent_find_rid
    lbl_find_rid = tk.Label(master=frm_form, text="Введите номер комнаты:")
    ent_find_rid = tk.Entry(master=frm_form, width=50)
    lbl_find_rid.grid(row=0, column=0, sticky="e")
    ent_find_rid.grid(row=0, column=1)

    global ent_find_class
    lbl_find_class = tk.Label(master=frm_form, text="Тип комнаты:")
    ent_find_class = tk.Entry(master=frm_form, width=50)
    lbl_find_class.grid(row=1, column=0, sticky="e")
    ent_find_class.grid(row=1, column=1)

    global ent_find_free
    lbl_find_free = tk.Label(master=frm_form, text="Свободна:")
    ent_find_free = tk.Entry(master=frm_form, width=50)
    lbl_find_free.grid(row=2, column=0, sticky="e")
    ent_find_free.grid(row=2, column=1)

    global ent_find_clean
    lbl_find_clean = tk.Label(master=frm_form, text="Убрана:")
    ent_find_clean = tk.Entry(master=frm_form, width=50)
    lbl_find_clean.grid(row=3, column=0, sticky="e")
    ent_find_clean.grid(row=3, column=1)

    global ent_find_repair
    lbl_find_repair = tk.Label(master=frm_form, text="Нуждается в ремонте:")
    ent_find_repair = tk.Entry(master=frm_form, width=50)
    lbl_find_repair.grid(row=4, column=0, sticky="e")
    ent_find_repair.grid(row=4, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    global rtext
    rtext = tk.Text(width=100, height=15)
    rtext.pack()

    btn1 = tk.Button(master=frm_buttons, text="Свободна", command=free)
    btn1.grid(row=0, column=0)
    btn2 = tk.Button(master=frm_buttons, text="Занята", command=notfree)
    btn2.grid(row=0, column=1)
    btn3 = tk.Button(master=frm_buttons, text="Убрана", command=clean)
    btn3.grid(row=1, column=0)
    btn4 = tk.Button(master=frm_buttons, text="Не убрана", command=notclean)
    btn4.grid(row=1, column=1)
    btn5 = tk.Button(master=frm_buttons, text="Нуждается в ремонте", command=repair)
    btn5.grid(row=2, column=0)
    btn6 = tk.Button(master=frm_buttons, text="Не нуждается в ремонте", command=notrepair)
    btn6.grid(row=2, column=1)
    btn7 = tk.Button(master=frm_buttons, text="Эконом", command=econom)
    btn7.grid(row=3, column=0)
    btn8 = tk.Button(master=frm_buttons, text="Комфорт", command=comfort)
    btn8.grid(row=3, column=1)
    btn9 = tk.Button(master=frm_buttons, text="Люкс", command=lux)
    btn9.grid(row=3, column=2)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти", command=find_room)
    btn_submit.grid(row=4, column=0)
    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.grid(row=4, column=1)
