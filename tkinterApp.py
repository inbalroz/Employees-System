import tkinter as tk
from tkinter import ttk
from tkinter import *
import created_employes
import attendance_log
import delete_employee
import search_employee_by_id

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self) # creating a container
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}  # initializing frames to an empty array
        self.different_pages()

    def different_pages(self):
        for F in (created_employes.created_employes, attendance_log.attendance_log, delete_employee.delete_employee, search_employee_by_id.search_employee_by_id): # iterating through a tuple consisting of the different page layouts
            frame = F(self.container, self)
            self.frames[F] = frame # initializing frame of that object from startpage, page1, page2 respectively with for loop
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(created_employes.created_employes)
    def show_frame(self, cont): #to display the current frame passed as parameter
        frame = self.frames[cont]
        frame.tkraise()