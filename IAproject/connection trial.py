from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from mysql.connector import Error
from tkinter import ttk



root = Tk()
root.title('Y12 MySQL Example')
root.geometry('800x800')

tabParent = ttk.Notebook(root)
tab1 = ttk.Frame(tabParent)
tab2 = ttk.Frame(tabParent)

tabParent.add(tab1, text="Add a record")
tabParent.add(tab2, text="Delete a record")


# Server conn check and info
try:
    db = mysql.connector.connect(host="192.168.64.3", user="22TinnaM", password="test", database="test")
    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()
    dbInfo = db.get_server_info()
    dbConn = cur.fetchone()
    messagebox.showinfo("Database connection", "SUCCESS!  Connected to MySQL Server " + dbInfo)
except Error as e:
    messagebox.showinfo("Database connection failed")


# Basic search all DB and list
def searchAll():
    db = mysql.connector.connect(host="192.168.64.3", user="22TinnaM", password="test", database="test")  # name of the data base

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    # executing queries
    cur.execute("SELECT * FROM gen_info")

    # basic query
    records = cur.fetchall()

    print_records = ' '
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\n"

    txtLabel = Label(root, text=print_records)
    txtLabel.grid(row=5, columnspan=4)

    # commit changes
    db.commit()

    # Always close the DB connection
    db.close()


# Add student Screen
def addStudent():
    editor = Tk()
    editor.title('Editor: ADD Students')
    #editor.geometry('400x400')

    # Close button
    def killWin():
        editor.destroy()

    # ADD button
    def addExec():
        db = mysql.connector.connect(host="192.168.64.3", user="22TinnaM", password="test", database="test")  # name of the data base

        # you must create a Cursor object. It will let you execute all the queries you need
        cur = db.cursor()

        # trying to add/insert the record
        try:
            sql = 'INSERT INTO `gen_info` (firstName, lastName, yearLevel, schoolID) VALUES (%s, %s, %s, %s)'
            values = (txtFName.get(), txtLName.get(), txtYear.get(), txtID.get())
            cur.execute(sql, values)
            db.commit()
            db.close()
            messagebox.showinfo("Database Add Student", "SUCCESS! Record entered at ID" + str(cur.lastrowid))
        except Error as e:
            messagebox.showinfo("Database Add Student", "FAILED!")
            print(e)
            db.close()
        # regardless of success or failed delete all the text from entry
        finally:
            txtFName.delete(0,END)
            txtLName.delete(0,END)
            txtYear.delete(0,END)
            txtID.delete(0,END)

    # basic layout - labels and entry boxes for db
    lblFName=Label(editor, text="First Name")
    txtFName = Entry(editor, width=20)
    lblFName.grid(row=1, column=0)
    txtFName.grid(row=1, column=1)

    lblLName = Label(editor, text="Last Name")
    txtLName = Entry(editor, width=20)
    lblLName.grid(row=2, column=0)
    txtLName.grid(row=2, column=1)

    lblYear = Label(editor, text="Year level")
    txtYear = Entry(editor, width=20)
    lblYear.grid(row=3, column=0)
    txtYear.grid(row=3, column=1)

    lblID = Label(editor, text="School ID")
    txtID = Entry(editor, width=20)
    lblID.grid(row=4, column=0)
    txtID.grid(row=4, column=1)

    btnAdd = Button(editor, text="ADD", command=addExec)
    btnAdd.grid(row=5, column=1)
    btnKill = Button(editor, text="Close", command=killWin)
    btnKill.grid(row=5, column=0)


# Edit / Update student info page
def editStudent():
    editor = Tk()
    editor.title = ("A new world...")
    editor.geometry("400x400")

    def killWin():
        editor.destroy()

    btnKill = Button(editor, text="Close", command=killWin)
    btnKill.pack()

# delete student record page
def delStudent():
    editor = Tk()
    editor.title = ("A new world...")
    editor.geometry("400x400")

    def killWin():
        editor.destroy()

    btnKill = Button(editor, text="Kill me", command=killWin)
    btnKill.pack()

btnSearch = Button(root,text="Search",command=searchAll)
btnSearch.grid(row=3,column=0)

btnNew = Button(root,text="ADD Student",command=addStudent)
btnNew.grid(row=3,column=1)

btnEdit = Button(root,text="EDIT Student",command=editStudent)
btnEdit.grid(row=3,column=2)

btnDel = Button(root,text="DELETE Student",command=delStudent)
btnDel.grid(row=3,column=3)



# basic layout - labels and entry boxes for db
lblFName=Label(tab1, text="First Name")
txtFName = Entry(tab1, width=20)
lblFName.grid(row=1, column=0)
txtFName.grid(row=1, column=1)

lblLName = Label(tab1, text="Last Name")
txtLName = Entry(tab1, width=20)
lblLName.grid(row=2, column=0)
txtLName.grid(row=2, column=1)

lblYear = Label(tab1, text="Year level")
txtYear = Entry(tab1, width=20)
lblYear.grid(row=3, column=0)
txtYear.grid(row=3, column=1)

lblID = Label(tab1, text="School ID")
txtID = Entry(tab1, width=20)
lblID.grid(row=4, column=0)
txtID.grid(row=4, column=1)

btnAdd = Button(tab1, text="ADD")
btnAdd.grid(row=5, column=1)
btnKill = Button(tab1, text="Close")
btnKill.grid(row=5, column=0)

tabParent.grid()

root.mainloop()
