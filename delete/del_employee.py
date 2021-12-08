from connect import *
import tkinter as tk
from tkinter import messagebox
from tables.client import *


# очистка полей ввода
def clear():
    ent_del_ename.delete(0, last='end')
    ent_del_eid.delete(0, last='end')


def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return "error"


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


def find_employee_id():
    global employee_id
    global ent_del_eid
    try:
        del_employee = f"""
                DELETE FROM
                employee
                WHERE
                employeeId={ent_del_eid.get()};
                """
        employee_id = execute_query(connection, del_employee)
        messagebox.showinfo("ОК", "Сотрудник удален")
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")


def find_employee_name():
    global employee_name
    global ent_del_ename
    if get_text(ent_del_ename.get()) != "error":
        del_employee = f"""
                DELETE FROM
                employee
                WHERE
                fullName LIKE '%{ent_del_ename.get()}%';
                """
        employee_name = execute_query(connection, del_employee)
        messagebox.showinfo("ОК", "Сотрудник удален")
    else:
        messagebox.showinfo("Ошибка!", "Заполните поле")
    return 0


def del_ewindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для удаления сотрудника
    global ent_del_eid
    lbl_find_eid = tk.Label(master=frm_form, text="Введите ID сотрудника:")
    ent_del_eid = tk.Entry(master=frm_form, width=50)
    lbl_find_eid.grid(row=0, column=0, sticky="e")
    ent_del_eid.grid(row=0, column=1)

    global ent_del_ename
    lbl_find_ename = tk.Label(master=frm_form, text="Введите ФИО сотрудника:")
    ent_del_ename = tk.Entry(master=frm_form, width=50)
    lbl_find_ename.grid(row=1, column=0, sticky="e")
    ent_del_ename.grid(row=1, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Удалить по id", command=find_employee_id)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Удалить по имени", command=find_employee_name)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
