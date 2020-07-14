import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd

import created_employes
import delete_employee
import search_employee_by_id

#attendance log

class attendance_log(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='light green') # backround
        self.controller.geometry("800x500")
        w = Label(self, text='Attendance log', bg="light green", fg="black", font=30)
        w.grid(row=1, column=1, pady=10)
        self.lates_or_all()
        self.year_box()
        self.month_box()
        self.ID_box()
        self.design_page_one()
        self.button()

    def lates_or_all(self):
        OPTIONS = [
            "select info",
            "Lates"
        ]
        self.lates = StringVar(self)# default value
        x = self.lates.set('select info')
        w_option_box = OptionMenu(self, self.lates, *OPTIONS)
        w_option_box.grid(row=2, column=1,columnspan=4, sticky=W, pady=10, padx = 5)

    def read_new_year(self): #Every year need to refresh the new year
        self.df = pd.read_excel('computer clock.xlsx')
        all_years = self.df['YEAR'].tolist()
        filter_years = []
        for i in all_years:
            if i not in filter_years:
                filter_years.append(i)
        filter_years.sort()
        filter_years = [str(i) for i in filter_years]
        return filter_years

    def year_box(self):
        filter_years = self.read_new_year()
        OPTIONS = ["select year",
                   "2019"]
        OPTIONS.append(filter_years[-1])
        self.chosen_year = StringVar(self)
        y = self.chosen_year.set('2020')  # default value
        w = OptionMenu(self, self.chosen_year, *OPTIONS)
        w.grid(row=2, column=1, columnspan=4, sticky=N, pady=10, padx = 5)

    def month_box(self):
        OPTIONS = [
            "select month",
            "DEC",
            "OCT"
        ]
        self.chosen_month = StringVar(self)
        z = self.chosen_month.set('select month')  # default value
        w = OptionMenu(self, self.chosen_month, *OPTIONS)
        w.grid(row=2, column=1, columnspan=4, sticky=E, pady=10, padx = 5)

    def design_page_one(self):
        Filter = Label(self, text="Filter", bg="light green", fg="red")
        Filter.grid(row=2, column=0)
        id = Label(self, text="ID", bg="light green")
        id.grid(row=3, column=1, columnspan=2, sticky = NW, rowspan = 1)
        self.T = Text(self, height = 20, width = 50)
        self.T.grid(row=4, column=0, padx=10, columnspan=4, rowspan=4,
               sticky=W+E+N+S)

    def write_to_txt_box(self, S):
        self.T.insert(END, S)
        sys.stdout = self.T

    def clear_txt_box(self):
        self.T.delete("1.0", END)

    def focus1(self):
        # set focus on the course_field box
        self.id.focus_set()

    def ID_box(self):
        self.id = Entry(self)
        self.id.bind("<Return>", self.focus1)
        self.id.grid(row=3, column=1, columnspan=2, sticky = N, rowspan = 1)

    def clear_id_box(self):  # clear the content of box after clicked the button
        self.id.delete(0, END)

    def create_dataframe(self): #filter results
        self.Lates = self.lates.get()
        self.Chosen_year = self.chosen_year.get()
        self.Chosen_month = self.chosen_month.get()
        self.ID = self.id.get()
        x = pd.read_excel('computer clock.xlsx')
        self.df2 = pd.read_excel('excel.xlsx')
        x = x[x['ID'].isin(self.df2['ID'])]

        if self.Chosen_month != 'select month':
            x = x[x['MONTH'] == self.Chosen_month]
        if self.Chosen_year != 'select year':
            x = x[x['YEAR'] == int(self.Chosen_year)]
        if self.Lates != 'select info':
            x = x[x['TOTAL'] < 8]
        if self.ID != '':
            x = x[x['ID'] == int(self.ID)]

        self.clear_id_box()
        self.df = x
        self.clear_txt_box()
        self.write_to_txt_box(self.df.to_string(index=False))

    def export_to_excel_file(self):
        with pd.ExcelWriter('excel.xlsx') as writer:
            self.df2.to_excel(writer, sheet_name = 'Employees',index=False)
            self.df.to_excel(writer, sheet_name='attendance log', index=False)

    def button(self):
        search= ttk.Button(self, text='search', command=self.create_dataframe)
        search.grid(row=3, column=5,columnspan=2, sticky=E, pady=10, padx = 5)
        export_to_excel_file = ttk.Button(self, text='export to excel file', command=self.export_to_excel_file)
        export_to_excel_file.grid(row=4, column=5, columnspan=2, sticky=E, pady=10, padx=5)
        button1 = ttk.Button(self, text="creat employee",
                             command=lambda: self.controller.show_frame(created_employes.created_employes))
        button1.grid(row=5, column=5,columnspan=2, sticky = SE, padx=10)
        button2 = ttk.Button(self, text="delete employee",
                             command=lambda: self.controller.show_frame(delete_employee.delete_employee))
        button2.grid(row=6, column=5, columnspan=2, sticky = SE, padx=10)

        button3 = ttk.Button(self, text="search employee",
                             command=lambda: self.controller.show_frame(search_employee_by_id.search_employee_by_id))
        button3.grid(row=7, column=5,columnspan=2, sticky = SE, padx=10)

