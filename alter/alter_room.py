import tkinter as tk
from tkinter import messagebox
from tables.employee import *

lbl2_post = 0
lbl2_hotel = 0


# очистка полей ввода
def clear():
    ent_id.delete(0, last='end')
    ent_free.delete(0, last='end')
    ent_clean.delete(0, last='end')
    ent_repair.delete(0, last='end')


def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return ""


# добавление атрибутов в запрос
def change():
    global alter_e
    if get_text(ent_free.get()) != '':
        if get_text(ent_free.get()) == 'да':
            alter_e += "isFree=1, "
        if get_text(ent_free.get()) == 'нет':
            alter_e += "isFree=0, "
    if get_text(ent_clean.get()) != '':
        if get_text(ent_clean.get()) == 'да':
            alter_e += "isCleaned=1, "
        if get_text(ent_clean.get()) == 'нет':
            alter_e += "isCleaned=0, "
    if get_text(ent_repair.get()) != '':
        if get_text(ent_repair.get()) == 'да':
            alter_e += "needToRepair=1, "
        if get_text(ent_repair.get()) == 'нет':
            alter_e += "needToRepair=0, "
    alter_e = alter_e[0:len(alter_e) - 2] + f" WHERE numberOfRoom={ent_id.get()};"


# изменение сотрудника
def alter_click():
    global alter_e
    if get_text(ent_id.get()) != "":
        alter_e = "UPDATE room SET "
        change()
        execute_query(connection, alter_e)
        messagebox.showinfo("ОК!", "Состояние комнаты изменено")
        clear()
    else:
        messagebox.showinfo("Ошибка!", "Введите корректный номер комнаты")


# заполнение полей
def free():
    global ent_free
    ent_free.delete(0, last='end')
    ent_free.insert(0, 'да')


def notfree():
    global ent_free
    ent_free.delete(0, last='end')
    ent_free.insert(0, 'нет')


def clean():
    global ent_clean
    ent_clean.delete(0, last='end')
    ent_clean.insert(0, 'да')


def notclean():
    global ent_clean
    ent_clean.delete(0, last='end')
    ent_clean.insert(0, 'нет')


def repair():
    global ent_repair
    ent_repair.delete(0, last='end')
    ent_repair.insert(0, 'да')


def notrepair():
    global ent_repair
    ent_repair.delete(0, last='end')
    ent_repair.insert(0, 'нет')


def alter_rwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для изменения сотрудника
    global ent_id
    lbl_id = tk.Label(master=frm_form, text="Номер комнаты:")
    ent_id = tk.Entry(master=frm_form, width=50)
    lbl_id.grid(row=0, column=0, sticky="e")
    ent_id.grid(row=0, column=1)
    global ent_free
    lbl_free = tk.Label(master=frm_form, text="Свободна:")
    ent_free = tk.Entry(master=frm_form, width=50)
    lbl_free.grid(row=1, column=0, sticky="e")
    ent_free.grid(row=1, column=1)

    global ent_clean
    lbl_clean = tk.Label(master=frm_form, text="Убрана:")
    ent_clean = tk.Entry(master=frm_form, width=50)
    lbl_clean.grid(row=2, column=0, sticky="e")
    ent_clean.grid(row=2, column=1)

    global ent_repair
    lbl_repair = tk.Label(master=frm_form, text="Нуждается в ремонте:")
    ent_repair = tk.Entry(master=frm_form, width=50)
    lbl_repair.grid(row=3, column=0, sticky="e")
    ent_repair.grid(row=3, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
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

    frm_submit = tk.Frame()
    frm_submit.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_submit, text="Изменить", command=alter_click)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_submit, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
