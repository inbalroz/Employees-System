import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import created_employes
import attendance_log
import delete_employee

class search_employee_by_id(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global uid
        LARGEFONT = ("Verdana", 25)
        self.controller = controller
        label = ttk.Label(self, text="search by id", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)
        x = tk.Label(self, text="User ID", bg="blue", fg="white")
        x.grid(row=4, column=1, padx=0, pady=0)
        self.vcmd = (self.register(self.validate_only_numbers),
                     '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.button()

    def validate_only_numbers(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        # action=1 -> insert
        if (action == '1'):
            if text in '0123456789-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    def id_search_window(self):
        self.id = Entry(self, validate = 'key', validatecommand = self.vcmd)
        self.id.bind("<Return>", self.focusid)
        self.id.grid(row=5, column=1, padx=0, pady=0)

    def clear_id_search(self):
        # clear the content of text entry box
        self.id.delete(0, END)

    def error(self):
        error = tk.Tk()
        error.title('Error')
        ww = Label(error, text='Error!')
        button = tk.Button(error, text='ok', width=25, command=error.destroy)
        ww.pack()
        button.pack()

    def connect_xlsx_to_dataframe(self):
        self.df = pd.read_excel('excel.xlsx')

    def get_id_to_search(self):
        self.id_get = int(self.id.get())

    def search_employee(self):
        self.connect_xlsx_to_dataframe()
        self.get_id_to_search()
        res = self.id_get in self.df['ID'].values
        if res:
            self.employee_info = self.df.loc[self.df['ID'] == self.id_get]
            self.show_employee_data()
        else:
            self.error()
        self.clear_id_search()

    def focusid(self):
        self.id.focus_set()

    def show_employee_data(self):
       employee_data = tk.Tk()
       employee_data.title('Details:')
       w = Label(employee_data, text=str(self.employee_info))
       w.pack()
       button = tk.Button(employee_data, text='ok', width=25, command=employee_data.destroy)
       button.pack()

    def button(self):
        self.id_search_window()
        button = Button(self, text="search", command=self.search_employee)
        button.grid(row=6, column=1, padx=0, pady=0)

        button1 = ttk.Button(self, text="attendance log",
                             command=lambda: self.controller.show_frame(attendance_log.attendance_log))

        button1.grid(row=8, column=2)

        # button to show frame 3 with text
        button2 = ttk.Button(self, text="create employee",
                             command=lambda: self.controller.show_frame(created_employes.created_employes))
        button2.grid(row=7, column=2)

        button3 = ttk.Button(self, text="delete employee",
                             command=lambda: self.controller.show_frame(delete_employee.delete_employee))
        button3.grid(row=9, column=2)