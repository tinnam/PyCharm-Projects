from tkinter import *
from tkinter import messagebox
from functools import partial
import mysql.connector

global usernameEntry
global passwordEntry

#clear username + password function


#creating login page window
root=Tk()
root.resizable=(False,False)
#default window size of window
root.geometry('1305x780')
#title of login window
root.title ('Login Page')
#login page text
top_title=Label( text="Login Page", font= 'Opensans 60', bg='#fcf1ef', fg='black')\
    .place(x=500, y=10)

#username text and input box
usernameLabel = Label(root, text="User Name:",font='Opensans 30').place(x=350, y=200)
username = StringVar()
usernameEntry = Entry(root, font='Opensans 20', textvariable=username, bg='#EFF0F1')\
    .place(x=600, y=200, height=40)

#password text and input box
passwordLabel = Label(root, text="Password:",font='Opensans 30').place(x=350, y=300)
password = StringVar()
passwordEntry = Entry(root, font='Opensans 20', textvariable=password, bg='#EFF0F1')\
    .place(x=600, y=300, height=40)

def deleteuserpass():
    print("Test delete")
    #usernameEntry.delete(0, 'end)
    #passwordEntry.delete(0, 'end')
    usernameEntry.set("test delete")


#hide password check button
var1=IntVar()
def hidepass():
    if var1.get() == 1:
        passwordEntry = Entry(root, textvariable=password, show='*',font='Opensans 20',
                              bg='#EFF0F1').place(x=600, y=300, height=40)
    else:
        passwordEntry = Entry(root, textvariable=password, font='Opensans 20', bg='#EFF0F1')\
            .place(x=600, y=300, height=40)
hidepassbutton=Checkbutton(root,text="hide pass", font='Opensans 20', onvalue=1, variable=var1,
                           command=hidepass).place(x=760,y=350)

#validating password, checking if it matches databse
def validateLogin(username, password):
    mydb = mysql.connector.connect(
        host="192.168.64.3",
        user="22TinnaM	",
        password="test",
        # port=3307,
        database="test"
    )
    mycursor = mydb.cursor()
    username.get()
    password.get()
    #finding values from the specific user table
    sql = "select * from userprofile where User_ID = %s and Password = %s"
    mycursor.execute(sql,[(username.get()),(password.get())])
    results = mycursor.fetchall()
    #ssucessful, then transfer to homepage
    if results:
        for i in results:
            messagebox.showinfo("Error", "Successfully logged in")
            root.destroy()
            import homepage
            break
    else:
        messagebox.showinfo("Error", "Incorrect password. Please try again")
        deleteuserpass()

#login button + passing value
validateLogin= partial(validateLogin, username, password)
loginbutton=Button(root,text="Login",font='Opensans 20',command=validateLogin, height=2,
                   width=12).place(x=713,y=400)




root.mainloop()