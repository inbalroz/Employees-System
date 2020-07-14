import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import created_employes
import attendance_log
import search_employee_by_id


class delete_employee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global udelete
        LARGEFONT = ("Verdana", 25)
        self.controller = controller
        self.configure(background='light green')
        label = ttk.Label(self, text="delete employee", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)
        x = tk.Label(self, text="User ID", bg="blue", fg="white")
        x.grid(row=4, column=1, padx=0, pady=0)
        self._delete_window()
        self.button()

    def focusdel(self):
        self.delete.focus_set()

    def connect_xlsx_to_dataframe(self):
        self.df = pd.read_excel('excel.xlsx')

    def import_id_to_delete(self):
        self.d = self.delete.get()

    def clear(self):  # clear the content of box after clicked the bottun
        self.delete.delete(0, END)

    def delete_employee_from_excel(self):
        self.connect_xlsx_to_dataframe()
        self.import_id_to_delete()
        self.df = self.df[self.df['ID'] != int(self.d)]
        self.df.to_excel('excel.xlsx', sheet_name='Employees', index=False)
        self.clear()

    def clear_id(self):
        # clear the content of text entry box
        self.delete.delete(0, END)

    def _delete_window(self):
        self.delete = tk.Entry(self)
        self.delete.bind("<Return>", self.focusdel)
        self.delete.grid(row=5, column=1, padx=0, pady=0)

        udelete = self.delete.get()

    def button(self):
        button = Button(self, text="delete employee", command=self.delete_employee_from_excel)
        button.grid(row=6, column=1, padx=0, pady=0)

        button1 = ttk.Button(self, text="attendance log",
                             command=lambda: self.controller.show_frame(attendance_log.attendance_log))

        button1.grid(row=8, column=2, padx=10, pady=10)

        button2 = ttk.Button(self, text="creat employee",
                             command=lambda: self.controller.show_frame(created_employes.created_employes))
        button2.grid(row=7, column=2, padx=10, pady=10)
        button3 = ttk.Button(self, text="search employee",
                             command=lambda: self.controller.show_frame(search_employee_by_id.search_employee_by_id))
        button3.grid(row=9, column=2, padx=10, pady=10)