from connect import *
import tkinter as tk
from tkinter import messagebox


# очистка полей ввода
def clear():
    ent_find_gid.delete(0, last='end')


def get_text(tmp):
    if tmp != "":
        return tmp
    else:
        return "error"


# транформация имени
def name(tmp):
    f_name = f"""
            SELECT fullName FROM
            client
            WHERE
            clientId={tmp};
            """
    tmp = execute_read_query(connection, f_name)[0][0]
    return tmp


# нахождение по ID
def find_guest_id():
    global guest_id
    global ent_find_gid
    global gtext
    try:
        gtext.delete('1.0', 'end')
        find_client = f"""
                SELECT * FROM
                guest
                WHERE
                clientId={ent_find_gid.get()};
                """
        gtext.insert('1.0', 'ID ФИО Карта Комната Счет Время прибытия Время отбытия\n')
        guest_id = execute_read_query(connection, find_client)
        tmp = [guest_id[0][0], name(guest_id[0][0]), guest_id[0][1], guest_id[0][2], guest_id[0][3], guest_id[0][4],
               guest_id[0][5]]
        gtext.insert('2.0', tmp)
    except:
        messagebox.showinfo("Ошибка!", "Неверно заполнено поле")


# нахождение по имени
def find_guest_name():
    global guest_name
    global gtext
    gtext.delete('1.0', 'end')
    find_employee = """
                SELECT * FROM
                guest;
                """
    guest_name = execute_read_query(connection, find_employee)
    gtext.insert('1.0', 'ID ФИО Карта Комната Счет Время прибытия Время отбытия\n')
    for i in guest_name:
        tmp = [i[0], name(i[0]), i[1], i[2], i[3], str(i[4]), str(i[5])]
        gtext.insert('end', f'{tmp}\n')
    return 0


def find_gwindow():
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack(side=tk.TOP)

    # названия и поля для нахождения постояльца
    global ent_find_gid
    lbl_find_gid = tk.Label(master=frm_form, text="Введите ID клиента:")
    ent_find_gid = tk.Entry(master=frm_form, width=50)
    lbl_find_gid.grid(row=0, column=0, sticky="e")
    ent_find_gid.grid(row=0, column=1)

    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    global gtext
    gtext = tk.Text(width=100, height=15)
    gtext.pack()

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Найти", command=find_guest_id)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка отправки
    btn_submit = tk.Button(master=frm_buttons, text="Вывести всех", command=find_guest_name)
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    # кнопка очистки
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear)
    btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)
