from auth import *


def log():
    window.destroy()
    login()


window = tk.Tk()
window.title('Добро пожаловать')
window.geometry('400x150')
window.resizable(False, False)

frm_lbl = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
frm_lbl.pack(fill=tk.X)
lbl_name = tk.Label(master=frm_lbl, text="Выберите опцию:", width=20, height=1)
lbl_name.pack(side=tk.BOTTOM)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=10)

btn_auth = tk.Button(master=frm_buttons, text="Авторизация", command=log, width=20, height=1)
btn_auth.pack(side=tk.TOP, pady=5, ipady=5)

# запускаем главный цикл окна
window.mainloop()
