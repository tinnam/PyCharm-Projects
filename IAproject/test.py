# print(u'H\u2082SO\u2084')
# print("x\u2015 + °C y\u207B\u00B9 = 2")  # x² + y² = 2
#
# import mysql.connector
# import codecs
#
# mydb = mysql.connector.connect(
#   host="192.168.64.3",
#   user="22TinnaM	",
#   password="test",
#   # port=3307,
#   database="test"
# )
# cursor = mydb.cursor()
# cursor.execute("SELECT * FROM testpastpaper")
# results=cursor.fetchall()
# print(results)
#


from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector
from tkinter import *


# s = Style()
# s.theme_use('lumen')
# root = s.master
# root.title("Add questions")
# root.geometry('1400x780')
# def popup_bonus():
#     win =Toplevel(s.master)
#     win.wm_title("Window")
#
#     l = ttk.Label(win, text="Input")
#     l.grid(row=0, column=0)
#
#     b = ttk.Button(win, text="Okay", command=win.destroy)
#     b.grid(row=1, column=0)
#
#
# button =ttk.Button(root, text='button', command=popup_bonus())
# button.pack()
#
#
#
#
# root.mainloop()

# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
# from tkinter import *
# from tkinter.ttk import *
#
# # creates a Tk() object
# master=Tk()
#
# # sets the geometry of main
# # root window
# master.geometry("200x200")


# # function to open a new window
# # on a button click
# def openNewWindow():
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(master)
#
#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("New Window")
#
#     # sets the geometry of toplevel
#     newWindow.geometry("200x200")
#
#     # A Label widget to show in toplevel
#     Label(newWindow,
#           text="This is a new window").pack()
#
#
# label = Label(master,
#               text="This is the main window")
#
# label.pack(pady=10)
#
# # a button widget which will open a
# # new window on button click
# btn = Button(master,
#              text="Click to open a new window",
#              command=openNewWindow)
# btn.pack(pady=10)
#
# # mainloop, runs infinitely
# mainloop()
from tkinter import ttk
from ttkbootstrap import Style
from tkinter import *


# creates a Tk() object
s = Style()
s.theme_use('lumen')
root = s.master
root.title("Add questions")
root.geometry('1400x780')

root.geometry("200x200")

def openNewWindow():

    newWindow = Toplevel(root)
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()


label = Label(root,
              text="This is the main window")

label.pack(pady=10)
btn = Button(root,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)
mainloop()