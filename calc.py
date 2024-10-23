import tkinter
import tkinter as tk
from operator import index
import re


def is_valid(newval):
    return re.match("^\\d*$", newval) is not None


def get_values():
    num_1 = int(number_1_entry.get())
    num_2 = int(number_2_entry.get())
    return num_1, num_2


def insert_values(value):
    text_var.set('')
    text_var.set( value)


def add():
    num_1, num_2 = get_values()
    res = num_1 + num_2
    insert_values(res)


def sub():
    num_1, num_2 = get_values()
    res = num_1 - num_2
    insert_values(res)


def mul():
    num_1, num_2 = get_values()
    res = num_1 * num_2
    insert_values(res)


def div():
    num_1, num_2 = get_values()
    res = round(num_1 / num_2, 2)
    insert_values(res)


def del_():
    number_1_entry.delete(0, "end")
    number_2_entry.delete(0, "end")
    text_var.set('')
    number_1_entry.focus()


window = tk.Tk()
window.title('Calculator')
window.geometry('350x350')
window.resizable(False, False)

check = (window.register(is_valid), "%P")
text_var = tk.StringVar()

button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=75, y=200)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=125, y=200)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=175, y=200)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=225, y=200)
button_del_ = tk.Button(window, text='C', width=2, height=2, command=del_)
button_del_.place(x=275, y=200)
number_1_entry = tk.Entry(window, width=28, validate="key", validatecommand=check)
number_1_entry.place(x=100, y=75)
number_1_entry.focus()
number_2_entry = tk.Entry(window, width=28, validate="key", validatecommand=check)
number_2_entry.place(x=100, y=150)
answer_entry = tk.Label(window, textvariable=text_var, anchor=tkinter.W, width=24, relief="sunken", background="#ffffff")
answer_entry.place(x=100, y=300)
number_1 = tk.Label(window, text = 'Введите первое число:')
number_1.place(x=100, y=50)
number_2 = tk.Label(window, text = 'Введите второе число:')
number_2.place(x=100, y=125)
answer = tk.Label(window, text = 'Ответ:')
answer.place(x=100, y=275)

window.mainloop()
