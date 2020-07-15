import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import os.path
import attendance_log
import delete_employee
import search_employee_by_id
import sys
import about
from tkinter.messagebox import *

class created_employes(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent) #create GUI
        LARGEFONT = ("Verdana", 25)
        self.controller.title('system') #uppertitle
        self.controller.geometry("800x500") #window size
        main_label = ttk.Label(self, text="create employee", font=LARGEFONT) #main label
        main_label.grid(row=0, column=1, padx=10, pady=10)
        self.vcmd = (self.register(self.validate_only_numbers),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.about_window()
        self.design_page_one()
        self.white_window()
        self.button()

    def focus1(self):
        # set focus on the course_field box
        self.id.focus_set()

    def focus2(self):
        # set focus on the sem_field box
        self.name.focus_set()

    def focus3(self):
        # set focus on the form_no_field box
        self.age.focus_set()

    def focus4(self):
        self.phone.focus_set()

    def focus5(self):
        self.position.focus_set()

    def design_page_one(self):
    #    self.design_excel()
        heading = Label(self, text="Form", bg="light green") #creat label of employee data
        id = Label(self, text="ID", bg="light green")
        name = Label(self, text="Name", bg="light green")
        age = Label(self, text="Age", bg="light green")
        phone = Label(self, text="Phone", bg="light green")
        position = Label(self, text="Position.", bg="light green")
        heading.grid(row=3, column=0, padx=10, pady=10) #label location
        id.grid(row=4, column=0)
        name.grid(row=5, column=0)
        age.grid(row=6, column=0)
        phone.grid(row=7, column=0)
        position.grid(row=8, column=0)

        self.T = Text(self, height = 10, width = 50)
        self.T.grid(row=4, column=2, columnspan=4, rowspan=4,
               sticky=W+E+N+S)

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

    def limit_entry(self, str_var, length): #age-2 numbers, phone- 9 numbers.
        def callback(str_var):
            c = str_var.get()[0:length]
            str_var.set(c)

        str_var.trace("w", lambda name, index, mode, str_var=str_var: callback(str_var))

    def white_window(self): #create whites windows
        age = StringVar()
        phone = StringVar()

        self.limit_entry(age, 3)
        self.limit_entry(phone, 9)

        self.id = Entry(self, validate = 'key', validatecommand = self.vcmd)
        self.name = Entry(self)
        self.age = Entry(self, validate = 'key', validatecommand = self.vcmd, textvariable=age)
        self.phone = Entry(self, validate = 'key', validatecommand = self.vcmd, textvariable=phone)
        self.position = Entry(self)

        self.id.bind("<Return>", self.focus1) #whenever the enter key is pressed then call the focus function
        self.name.bind("<Return>", self.focus2)
        self.age.bind("<Return>", self.focus3)
        self.phone.bind("<Return>", self.focus4)
        self.position.bind("<Return>", self.focus5)

        self.id.grid(row=4, column=1)  #grid method is used for placing the widgets at respective positions in table like structure .
        self.name.grid(row=5, column=1)
        self.age.grid(row=6, column=1)
        self.phone.grid(row=7, column=1)
        self.position.grid(row=8, column=1)

    def clear(self):  # clear the content of box after clicked the button
        self.id.delete(0, END)
        self.name.delete(0, END)
        self.age.delete(0, END)
        self.phone.delete(0, END)
        self.position.delete(0, END)

    def error(self, type='missing_details'): #open error window if something is missing
        error = tk.Tk()
        error.title('Error')
        button = tk.Button(error, text='ok', width=25, command=error.destroy)
        if type=='missing_details':
            w = Label(error, text='Sorry, you did not fill in all the details ')
            w.pack()
        elif type=='id_exists':
            w = Label(error, text='Sorry, ID already exist')
            w.pack()
        button.pack()

    def about_window(self):
        menu = Menu(self.controller)
        self.controller.config(menu = menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open...')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.quit)
        helpmenu = Menu(menu)
        Help = menu.add_cascade(label='Help', menu=helpmenu)
        menu_About = tk.Menu(Help, tearoff=False)
        menu_About.add_command(label='About', command=lambda: about.about)
        helpmenu.add_command(label='About', command=self.__about)

    def __about(self):
        showinfo("Notepad", "My name is Inbal Rozencweig and this is my final project"
                            " of \'python\' course at SheCodes organisation.")

    def check_exsist(self,file_path):
        return os.path.exists(file_path)

    def create_dataframe(self):
        if self.check_exsist('excel.xlsx'):
            self.df = pd.read_excel('excel.xlsx')
        else:
            self.df = pd.DataFrame(columns=['ID', 'Name', 'Age', 'Phone', 'Position'])

    def write_to_txt_box(self, S):
        self.T.insert(END, S.to_string(index=False))
        sys.stdout = self.T

    def clear_txt_box(self):
        self.T.delete("1.0", END)

    def insert(self):
        self.create_dataframe()
        self.selfs_list = [[self.id, self.name, self.age, self.phone, self.position]]
        self.get_values =[]
        for i in self.selfs_list[0]:
            self.get_values.append(i.get())
        s = self.id.get()
        res = id in self.df['ID'].values
        if "" in self.get_values:
            self.error()
        elif int(s) in self.df['ID'].values:
            self.error('id_exists')
            self.clear()
        else:
            self.add_list_get_values =  []
            self.add_list_get_values.append(self.get_values)
            self.df = self.df.append(pd.DataFrame(self.add_list_get_values,
                               index=[0],
                               columns=['ID', 'Name', 'Age', 'Phone', 'Position']))
            self.df.head()
            self.df.to_excel('excel.xlsx', sheet_name = 'Employees',index=False)
            self.write_to_txt_box(self.df)
            self.clear() #clear box
            self.clear_txt_box()
            self.write_to_txt_box(self.df)

    def refresh(self):
        self.df = pd.read_excel('excel.xlsx')
        self.clear_txt_box()
        self.write_to_txt_box(self.df)

    def export_txt_box_to_file(self):
        get_txt = self.T.get('1.0', 'end')
        write_txt_file = open('employees txt file.txt', 'w')
        write_txt_file.truncate(0)
        write_txt_file.write(get_txt)
        write_txt_file.close()

    def button(self):
        submit = Button(self, text="submit", fg="Black",
                        bg="Red", command=self.insert)
        submit.grid(row=9, column=1)
        button1 = ttk.Button(self, text="attendance log",
                             command=lambda: self.controller.show_frame(attendance_log.attendance_log))
        button1.grid(row=10, column=5)
        button2 = ttk.Button(self, text="delete employee",
                             command=lambda: self.controller.show_frame(delete_employee.delete_employee))
        button2.grid(row=11, column=5)
        button3 = ttk.Button(self, text="search employee",
                             command=lambda: self.controller.show_frame(search_employee_by_id.search_employee_by_id))
        button3.grid(row=12, column=5)
        refresh = Button(self, text="refresh", command= self.refresh)
        refresh.grid(row=8, column=2, padx=10, pady=10)
        export = Button(self, text="export to txt", command=self.export_txt_box_to_file)
        export.grid(row=8, column=3, padx=10, pady=10)




