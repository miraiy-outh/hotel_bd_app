from connect import *
import tkinter as tk
from tkinter import messagebox
from tables.client import *


# очистка полей ввода
def clear():
    ent_find_ename.delete(0, last='end')
    ent_find_eid.delete(0, last='end')


def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return "error"


# транформация названия должности
def post(tmp):
    f_post = f"""
            SELECT nameOfPost FROM
            post
            WHERE
            postId={tmp};
            """
    tmp = execute_read_query(connection, f_post)[0][0]
    return tmp


# транформация названия отеля
def hotel(tmp):
    f_hotel = f"""
                SELECT nameOfHotel FROM
                hotel
                WHERE
                hotelId={tmp};
                """
    tmp = execute_read_query(connection, f_hotel)[0][0]
    return tmp


# нахождение по ID
def find_employee_id():
    global employee_id
    global ent_find_eid
    global etext
    try:
        etext.delete('1.0', 'end')
        find_employee = f"""
                SELECT * FROM
                employee
                WHERE
                employeeId={ent_find_eid.get()};
                """
        etext.insert('1.0', 'ID Должность Отель Рабочие дни Зарплата ФИО Номер телефона\n')
        employee_id = execute_read_query(connection, find_employee)
        tmp = [employee_id[0][0], post(employee_id[0][1]), hotel(employee_id[0][2]), employee_id[0][3],
               employee_id[0][4], employee_id[0][5], employee_id[0][6]]
        etext.insert('2.0', tmp)
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")


# нахождение по имени
def find_employee_name():
    global employee_name
    global ent_find_ename
    global etext
    try:
        etext.delete('1.0', 'end')
        find_employee = f"""
                SELECT * FROM
                employee
                WHERE
                fullName LIKE '%{ent_find_ename.get()}%';
                """
        employee_name = execute_read_query(connection, find_employee)
        etext.insert('1.0', 'ID Должность Отель Рабочие дни Зарплата ФИО Номер телефона\n')
        for i in employee_name:
            tmp = [i[0], post(i[1]), hotel(i[2]), i[3], i[4], i[5], i[6]]
            etext.insert('end', f'{tmp}\n')
    except:
        messagebox.showinfo("Ошибка!", "Заполните поле")
    return 0


def find_ewindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для нахождения работника
    global ent_find_eid
    lbl_find_eid = tk.Label(master=frm_form, text="Введите ID сотрудника:")
    ent_find_eid = tk.Entry(master=frm_form, width=50)
    lbl_find_eid.grid(row=0, column=0, sticky="e")
    ent_find_eid.grid(row=0, column=1)

    global ent_find_ename
    lbl_find_ename = tk.Label(master=frm_form, text="Введите ФИО сотрудника:")
    ent_find_ename = tk.Entry(master=frm_form, width=50)
    lbl_find_ename.grid(row=1, column=0, sticky="e")
    ent_find_ename.grid(row=1, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    global etext
    etext = tk.Text(width=100, height=15)
    etext.pack()

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти по id", command=find_employee_id)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти по имени", command=find_employee_name)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
