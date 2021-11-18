import tkinter as tk
import tkinter
from tkinter import ttk
from ttkbootstrap import Style
from ttkwidgets import CheckboxTreeview
from tkinter import *

s = Style()
s.theme_use('lumen')
root =s.master
root.title("Add test")
root.geometry('1400x780')



#commands
def canceltest():
    root.destroy()
    import homepage

#widgets
ntlb=ttk.Label(root, text='New Test', font=('','40'))
ntlb.grid(row=0, column=0, padx=20, pady=10, sticky='ew')

namelb=ttk.Label(root, text='Name', font=('', '15'))
namelb.grid(row=1, column=0, padx=20, pady=10, sticky='ew')
nameentry=ttk.Entry(root, width=100)
nameentry.grid(row=2, column=0, padx=20, pady=10, sticky='ew', columnspan=20)

descriptionlb=ttk.Label(root, text='Description', font=('','15'))
descriptionlb.grid(row=3, column=0, padx=20, pady=10, sticky='ew')
descriptionbox=tk.Text(root, width=100, height=15)
descriptionbox.grid(row=4, column=0, padx=20, pady=10, sticky='ew',columnspan=20)


createtestbt=ttk.Button(root, text='Create test', style='success.TButton')
createtestbt.grid(row=5, column=0, padx=20, pady=10, sticky='nw')
orlb=ttk.Label(root, text='or')
orlb.grid(row=5, column=0, padx=100, pady=15,sticky='nw')
cancelbt=ttk.Button(root, text='Cancel', style='danger.Outline.TButton', command=canceltest)
cancelbt.grid(row=5, column=0, padx=110)

root.mainloop()


