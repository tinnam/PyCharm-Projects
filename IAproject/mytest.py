import mysql.connector
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from ttkwidgets import CheckboxTreeview
from tkinter import *
from tkinter import messagebox
import codecs
class MyTest:
    def __init__(self, test_nameid): #constructor
        self.s = Style()
        self.s.theme_use('lumen')
        self.s.configure('', font=('', '15'))
        self.s.configure('TCheckbutton', font=('',"15"))
        self.s.configure('TLabelframe.Label', font=('', '15'))
        self.s.configure('success.Outline.TButton', font=('','15'))
        self.s.configure('custom.TFrame', background='#EBFFF1')
        self.s.configure('TButton', font=('', '15'))
        self.s.configure('custom.TLabel', font=('', '15'), background='#EBFFF1', foreground='#0164B4')
        self.root = self.s.master
        self.root.title("Test Preview")
        self.root.geometry('1400x780')
        self.test_nameid=test_nameid

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.pack(fill='both', expand=1)
        self.canvas = Canvas(self.mainframe)
        self.canvas.pack(side='left', fill='both',expand=1)
        self.scrollbar = ttk.Scrollbar(self.mainframe, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.secondframe = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.secondframe, anchor='nw')
        #function to display or not display markscheme
        self.asp = tk.IntVar()
        self.ms = tk.IntVar()

        #test name title text
        self.testlb = ttk.Label(self.secondframe, text=self.getTestname(test_nameid),font=('', 40))
        self.testlb.pack(side='top', fill='x', padx=10, pady=30)
        #Add main boxed frame surrounding all edits
        self.mainframe = ttk.Labelframe(self.secondframe, text="All actions", padding=(20, 20, 10, 10),labelanchor='nw')
        self.mainframe.pack(anchor='w', side=TOP,padx=10, pady=30, fill=X, expand=False)
        #test preview options frame
        self.testpreviewframe = ttk.Labelframe(self.mainframe, text="preview options", padding=(20, 20, 10, 10))
        self.testpreviewframe.grid(row=0, column=0, padx=10,ipadx=40)
        self.answerspacebutton = ttk.Checkbutton(self.testpreviewframe, text='Answer space', onvalue=1, offvalue=0, variable=self.asp,command=lambda:self.showresults(self.ms.get(),self.asp.get()))
        self.answerspacebutton.grid(row=0, column=0, sticky='ew', padx=5, pady=10)
        self.markschemebutton = ttk.Checkbutton(self.testpreviewframe, text='Markscheme', onvalue=1, offvalue=0,variable=self.ms, command=lambda:self.showresults(self.ms.get(),self.asp.get()))
        self.markschemebutton.grid(row=1, column=0, sticky='ew', padx=5, pady=10)
        #edits frame
        self.addonframe = ttk.Labelframe(self.mainframe, text="edits", padding=(20, 20, 10, 10))
        self.addonframe.grid(row=0, column=1,padx=10,ipadx=40)
        self.addibquestions = ttk.Button(self.addonframe, text='add IB question', style='success.Outline.TButton')
        self.addibquestions.grid(row=0, column=0, sticky='ew', padx=5, pady=10)
        self.addownquestion = ttk.Button(self.addonframe, text='your own question', style='success.Outline.TButton')
        self.addownquestion.grid(row=1, column=0, sticky='ew', padx=5, pady=10)
        self.edittestname = ttk.Button(self.addonframe, text='edit test name and description', style='success.Outline.TButton')
        self.edittestname.grid(row=2, column=0, sticky='ew', padx=5, pady=10)
        # adding download features
        self.downloadframe = ttk.Labelframe(self.mainframe, text="download options", padding=(20, 20, 10, 10))
        self.downloadframe.grid(row=0, column=2, padx=10, ipadx=50)
        self.downloadpdf = ttk.Button(self.downloadframe, text='download as PDF')
        self.downloadpdf.grid(row=0, column=0, sticky='ew', padx=5, pady=10)
        self.downloaddocx = ttk.Button(self.downloadframe, text='download as docx')
        self.downloaddocx.grid(row=1, column=0, sticky='ew', padx=5, pady=10)
        self.printfile = ttk.Button(self.downloadframe, text='print file')
        self.printfile.grid(row=2, column=0, sticky='ew', padx=5, pady=10)
        # questions text
        # self.temptest = []
        # self.temptest = self.getTest(test_nameid)

        #creating new list from getTest function (separates the list to 3 indivual items)
        self.list1, self.list2, self.list3,self.list4 = self.getTest(test_nameid)
        #creating a list to define the object number
        self.msframe = []
        self.mslb=[]
        self.aspframe=[]
        self.asplb=[]
        print(self.list4 )
        #looping through the number of question in list to create new label frames + questions
        for q in range(0, len(self.list1)):
            self.bigframe = ttk.Labelframe(self.secondframe, padding=(20, 20, 10, 10))
            self.bigframe.pack(side=BOTTOM, fill=X, padx=10, pady=30, expand=False)
            self.questionframe = ttk.Frame(self.bigframe)
            self.questionframe.grid(sticky='ew', row=0, column=0)
            self.qlb = ttk.Label(self.questionframe, text=('Question:' + '\n' + self.list1[q]), style='TLabel',
                                     font=('', 15))
            self.qlb.grid(sticky='ew', row=0, column=0)
            self.answerframe = ttk.Frame(self.bigframe)
            self.answerframe.grid(sticky='ew', row=1, column=0)
            self.aclb = ttk.Label(self.answerframe,
                                      text=(self.list2[q]),
                                      style='TLabel', font=('', 15))
            self.aclb.grid(sticky='ew', row=0, column=0)
            #creating the markcheme frame + label by appending it into a list to make the obejct unique
            self.msframe.append(ttk.Frame(self.bigframe, style='custom.TFrame'))
            self.mslb.append(ttk.Label(self.msframe[q], text=('Markscheme:' + '\n' + self.list3[q]),
                                  font=('', 15), style='custom.TLabel'))
            # creating the answer space frame + label by appending it into a list to make the obejct unique
            self.aspframe.append(ttk.Frame(self.bigframe))
            self.asplb.append(ttk.Label(self.aspframe[q], text=self.list4[q],
                                   font=('', 15), style='TLabel'))
        self.root.mainloop()
    #function to allow the checkbutton in preview options to work
    def showresults(self, markscheme, answerspace):
        for q in range(0, len(self.list1)):
            #if marscheme is presses, show markscheme by griddinng pre existing objects in the list
            if markscheme == 1:
                self.msframe[q].grid(sticky='ew', row=3, column=0, columnspan=10, ipadx=200)
                self.mslb[q].grid(row=0, column=0, sticky='ew', columnspan=10)
            #if not checked or unchecked, un grid the object
            elif markscheme==0:
                self.msframe[q].grid_forget()
            if answerspace == 1:
                self.aspframe[q].grid(sticky='ew', row=2, column=0, columnspan=10)
                self.asplb[q].grid(row=0, column=0, sticky='ew', columnspan=10,pady=10)
            elif answerspace==0:
                self.aspframe[q].grid_forget()

    def getTestname(self, testid):
        self.mydb = mysql.connector.connect(host="192.168.64.3", user="22TinnaM", password="test", database="test")
        self.mycursor = self.mydb.cursor()
        self.sql = "select testname from mytests where testid = '" + testid + "'"
        print(self.sql)
        self.mycursor.execute(self.sql)
        self.results = self.mycursor.fetchone()
        print(self.results[0])
        return (self.results[0])
    def getTest(self, testid):
        self.mydb = mysql.connector.connect(host="192.168.64.3", user="22TinnaM", password="test", database="test")
        self.mycursor = self.mydb.cursor()
        self.sql="select list_questionid from mytests where testid = '"+testid+"'"
        print(self.sql)
        self.mycursor.execute(self.sql)
        self.results = self.mycursor.fetchall() #Output -> row
        self.temp = self.results[0][0]
        self.tempstr=""
        if "," in self.temp:
            self.listOfquestion=self.temp.split(',')
            print(self.listOfquestion)
            for i in range (len(self.listOfquestion)):
                if i == len(self.listOfquestion)-1:
                    self.tempstr = self.tempstr + "'" + self.listOfquestion[i]+ "'"
                else:
                    self.tempstr = self.tempstr + "'" + self.listOfquestion[i]+ "',"
            self.temp = self.tempstr
        else:
            self.temp = "'" + self.temp + "'"
        self.sql="select * from newpastpaper where No in ("+self.temp+")"
        print(self.sql)
        self.mycursor.execute(self.sql)
        self.results = self.mycursor.fetchall()
        self.qlist=[]
        self.aclist=[]
        self.mslist=[]
        self.aslist=[]
        #appending question text
        for i in self.results:
            self.qlist.append(i[1])
        # appending answer choice text
        for i in self.results:
            self.aclist.append(i[2])
        # appending markscheme text
        for i in self.results:
            self.mslist.append(i[3])
        #appending answer space
        for i in self.results:
            self.aslist.append(i[15])
        # print(self.mslist)
        # print(self.qlist)
        return self.qlist, self.aclist, self.mslist,self.aslist



MyTest('2')