import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from ttkwidgets import CheckboxTreeview
from tkinter import *
from tkinter import messagebox
import codecs

import databaseconnection
DB = databaseconnection.DBConnection()
import mytest


s = Style()
s.theme_use('lumen')
s.configure('TNotebook.Tab',font=('','15'))
s.configure('primary.Treeview', rowheight=40)
root =s.master
root.title("Homepage")
root.geometry('1400x780')

mainframe=ttk.Frame(root)
mainframe.pack(fill='both',expand=1)
canvas=Canvas(mainframe)
canvas.pack(side='left', fill='both', expand=1)
scrollbar=ttk.Scrollbar(mainframe, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
secondframe=ttk.Frame(canvas)
canvas.create_window((0,0),window=secondframe, anchor='nw')

# #creating the tab control
tabControl = ttk.Notebook(secondframe, width=1360, height=770)

#creating all tabs
qtab = tk.Frame(secondframe)
mttab = tk.Frame(secondframe)
tagstab = tk.Frame(secondframe)

#adding tabs to main frame
tabControl.add(qtab, text="Questions")
tabControl.add(mttab, text="My Tests")
tabControl.add(tagstab, text="Tags")

qtab.grid_columnconfigure((0,1),weight=1)
qtab.grid_columnconfigure((0,1),weight=1)
mttab.grid_rowconfigure((0,1),weight=1)
mttab.grid_rowconfigure((0,1),weight=1)
tabControl.grid(row=0, column=0, sticky='nsew')



#--------------------------------------------------- question tab
#treeview checkbox info
topics = ['1:Stoichiometric Relationships', '2:Atomic Structure', '3:Periodicity',
          '4:Chemical Bonding and Structure', '5:Energetics/Thermochemistry',
          '6:Chemical Kinetics', '7:Equilibrium', '8:Acids and Bases', '9:Redox Processes',
          '10:Organic Chemistry', '11: Measurement and Data Processing', '12:Atomic Structure (HL)',
          '13:The Periodic Table (HL)', '14:Chemical Bonding and Structure (HL)',
          '15:Energetics/Thermochemistry (HL)', '16:Chemical Kinetics (HL)', '17 Equilibrium (HL)',
          '18:Acids and Bases (HL)', '19:Redox Processes (HL)','20:Organic Chemistry (HL)',
          '21:Measurement and Analysis (HL)']

#all subtopics
subtopic = [['1.1:Introduction to the particulate nature of matter and chemical change',
            '1.2:The mole concept','1.3: Reacting masses and volumes'],['2.1:The nuclear atom',
            '2.2:Electron configuration'],['3.1:Periodic table','3.2:Periodic trends'],
           ['4.1:Ionic bonding and structure','4.2:Covalent bonding','4.3:Covalent structures',
            '4.4:Intermolecular forces','4.5:Metallic bonding'],['5.1:Measuring energy changes',
            '5.2:Hess’s Law','5.3:Bond enthalpies'],['6.1:Collision theory and rates of reaction'],
           ['7.1:Equilibrium'], ['8.1:Theories of acids and bases','8.2:Properties of acids and bases',
            '8.3:The pH scale', '8.4:Strong and weak acids and bases','8.5:Acid deposition'],
            ['9.1:Oxidation and reduction','9.2:Electrochemical cells'],['10.1:Fundamentals of organic chemistry',
            '10.2:Functional group chemistry'],['11.1:Uncertainties and errors in measurement and results',
            '11.2:Graphical techniques','11.3:Spectroscopic identification of organic compounds'],
            ['12.1:Electrons in atoms'],['13.1:First-row d-block elements','13.2:Coloured complexes'],
           ['14.1:Covalent bonding and electron domain and molecular geometries','14.2:Hybridization'],
           ['15.1:Energy cycles','15.2:Entropy and spontaneity'],['16.1:Rate expression and reaction mechanism',
            '16.2:Activation energy'],['17.1:The equilibrium law'],['18.1:Lewis acids and bases',
            '18.2:Calculations involving acids and bases','18.3:pH curves'],['19.1:Electrochemical cells'],
            ['20.1:Types of organic reactions','20.2:Synthetic routes','20.3:Stereoisomerism'],
           ['21.1:Spectroscopic identification of organic compounds']]

#date info
months = ('January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December')

years = ('2008', '2009', '2010', '2011', '2012', '2013',
        '2014', '2015', '2016', '2017', '2018', '2019','2020','2021')

testnames=DB.getTestnames()

#test info
test=()
#input variable
selectttopic = tk.StringVar()
searchqvar= tk.StringVar()
sllevel= tk.IntVar()
hllevel=tk.IntVar()
p1style=tk.IntVar()
p2style=tk.IntVar()
selecttag1= tk.StringVar()
selecttag2= tk.StringVar()
selecttag3= tk.StringVar()
selectmonth=tk.StringVar()
selectyear=tk.StringVar()
testname=tk.StringVar()
# searchalltest=tk.StringVar()


#commands
#navigate to tag tabs
def movetotagtab():
    tabControl.select(tagstab)
#navigate to add question window
def movetoaddq():
    root.destroy()
    import addquestion

#input field

# scrollbar = ttk.Scrollbar(root,orient='vertical')
# scrollbar.grid(row=0, column=10, sticky='ns')
input_labelframe = ttk.Labelframe(qtab, text='Search questions', padding=(20, 20, 10, 5))
input_labelframe.pack(side='top', fill='x', padx=10, pady=30)

searchlb= ttk.Label(input_labelframe, text='Search')
searchlb.grid(row=0, column=0, padx=3, sticky='ew')
searchentrybox = ttk.Entry(input_labelframe,textvariable=searchqvar, width=40)
searchentrybox.grid(row=0, column=1, padx=3, sticky='ew', columnspan=2)

def levelcheck():
    if sllevel.get()==1 and hllevel.get()==1:
        return'SL,HL'
    elif sllevel.get()==0 and hllevel.get()==1:
        return 'HL'
    elif hllevel.get()==0 and sllevel.get()==1:
        return'SL'
    elif hllevel.get()==0 and sllevel.get()==0:
        return'null'



levelframe=ttk.Labelframe(input_labelframe, text='Level',padding=(20, 10, 10, 5))
levelframe.grid(row=1, column=0, sticky='ew', columnspan=2, pady=10)
slcb=ttk.Checkbutton(levelframe,text='SL',variable=sllevel,onvalue=1,offvalue=0,
                     style='secondary.TCheckbutton', command=levelcheck)
slcb.grid(row=0, column=1, padx=3,pady=2, sticky='ew')
hlcb=ttk.Checkbutton(levelframe,text='HL',variable=hllevel,onvalue=1,offvalue=0,
                     style='secondary.TCheckbutton', command=levelcheck)
hlcb.grid(row=1, column=1, padx=3,pady=2, sticky='ew')

def paperstylecheck():
    if p1style.get() == 1 and p2style.get() == 1:
        return 'Paper 1,Paper 2'
    elif p1style.get() == 0 and p2style.get() == 1:
        return 'Paper 2'
    elif p2style.get() == 0 and p1style.get() == 1:
        return 'Paper 1'
    elif p2style.get() == 0 and p1style.get() == 0:
        return 'null'


paperframe=ttk.Labelframe(input_labelframe, text='Paper style',padding=(20, 10, 10, 5))
paperframe.grid(row=1, column=2, sticky='ew', columnspan=2, pady=10, padx=10)
p1cb=ttk.Checkbutton(paperframe,text='Paper 1',variable=p1style,onvalue=1,offvalue=0,
                     style='secondary.TCheckbutton')
p1cb.grid(row=0, column=2, padx=3,pady=2, sticky='ew')
p2cb=ttk.Checkbutton(paperframe,text='Paper 2',variable=p2style,onvalue=1,offvalue=0,
                     style='secondary.TCheckbutton')
p2cb.grid(row=1, column=2, padx=3,pady=2, sticky='ew')

tagframe=ttk.Labelframe(input_labelframe, text='Tags',padding=(20, 10, 10, 5))
tagframe.grid(row=1, column=4, sticky='ew', columnspan=4, pady=10, padx=10)
tog1box=ttk.Combobox(tagframe, textvariable=selecttag1, width=15)
tog1box.grid(row=0, column=0, padx=3, pady=5,sticky='ew')
tog2box=ttk.Combobox(tagframe, textvariable=selecttag2, width=15)
tog2box.grid(row=0, column=1, padx=3,pady=5,sticky='ew')
tog3box=ttk.Combobox(tagframe, textvariable=selecttag3, width=15)
tog3box.grid(row=0, column=2, padx=3,pady=5,sticky='ew')
edittagsbt=ttk.Button(tagframe, text='edit tags', style='warning.Outline.TButton', command=movetotagtab)
edittagsbt.grid(row=0, column=3, padx=3,pady=5,sticky='ew')

#question result treeview
questionresult=ttk.Treeview(qtab, style='primary.Treeview', height=10)
questionresult.pack(anchor='nw', fill='x', padx=10)
questionresult['columns'] = ('Question', 'Total marks', 'Last used')
questionresult.column('#0', width=0, stretch=NO)
questionresult.column('Question', width=600, anchor='center')
questionresult.column('Total marks', width=250, anchor='center')
questionresult.column('Last used', width=200, anchor='center')
questionresult.heading('#0', text='')
questionresult.heading('Question', text='Question')
questionresult.heading('Total marks', text='Total marks')
questionresult.heading('Last used',text='Last used')
#default view shows all of the questions before filter is added
if (len(DB.getAllquestion())) > 0:
    result = DB.getAllquestion()
for i in range(len(result)):
    questionresult.insert(parent='', index='end', iid=result[i][0], values=(
    result[i][1], result[i][11], result[i][13],))
#re updating the results everytime user presses search
def removeall():
    for record in questionresult.get_children():
        questionresult.delete(record)

def searchallq():
    removeall()
    a=treeviewClick()
    b=levelcheck()
    c=paperstylecheck()
    d = treeviewClicksub()
    result = []
    if (len(DB.getLevel_paperstyle_topic_sub(b,a,d,c))) >0:
        result = DB.getLevel_paperstyle_topic_sub(b,a,d,c)
    elif (len(DB.getLevel_paperstyle_topic(b,a,c))) >0:
        result=DB.getLevel_paperstyle_topic(b,a,c)
    elif(len(DB.getPaperstyle_topic(a,c)))>0:
        result= DB.getPaperstyle_topic(a,c)
    for i in range(len(result)):
        questionresult.insert(parent='', index='end', iid=result[i][0], values=(result[i][1],result[i][11],result[i][13], ))


def treeviewClick():  # Click
    list = []
    for item in topiclb.selection():
        item_text = topiclb.item(item, "values")
        list.append(item_text[0])
    return(list)  # Output the value of the first column of the selected row


def treeviewClicksub():  # Click
    list = []
    for item in topiclb.selection():
        item_text = topiclb.item(item, "values")
        list.append(item_text[0])
    return(list)  # Output the value of the first column of the selected row


searchbt=ttk.Button(input_labelframe, text='Search questions', command=searchallq)
searchbt.grid(row=2, column=5, sticky='nw', padx=10)
resetbt=ttk.Button(input_labelframe, text='Reset filters', style='Outline.TButton', command=removeall)
resetbt.grid(row=2, column=5, sticky='nw', padx=120)

tempSubTopic = []
with open('Chem_SubTopics.txt') as f:
    line = f.readlines()
    for lines in line:
        #remove newline or spacebar
        lines = lines.strip()
        tempSubTopic.append(lines)
        f.close()
counter = 0
arr_subtopic = []
subtopic = []
for i in range(0,len(tempSubTopic)):
    #assign number
    number_sub = tempSubTopic[i].split('.')
    number_topic = topics[counter].split(':')
    if(number_sub[0] == number_topic[0]):
        arr_subtopic.append(tempSubTopic[i])
    else:
        #print(arr_subtopic)
        subtopic.append(arr_subtopic)
        arr_subtopic = []
        arr_subtopic.append(tempSubTopic[i])
        counter = counter + 1
        if(i == len(tempSubTopic)-1):
            subtopic.append(arr_subtopic)
checkbox = dict()
for i in range(0,len(topics)):
       checkbox[topics[i]] = subtopic[i]
key_list = list(checkbox.keys())
value_list = list(checkbox.values())
#CheckboxTreeview
topiclb = ttk.Treeview(input_labelframe)
topiclb.grid(row=2, column=0, columnspan=4,rowspan=10, sticky='ew')
id = 22
#Change from 2 to be len(topics) after completed adding subtopics
for i in range(0,len(topics)):
    #Assign Topic
    topiclb.insert("", "end", i, text=key_list[i], values=(key_list[i], ))
    for j in range(0,len(value_list[i])):
        topiclb.insert(i, "end", id, text=value_list[i][j], values=(value_list[i][j], ))
        id = id + 1
#

# for i in range (len(allquestion)):
#     questionresult.insert(parent='', index='end', iid=allquestion[i][0], values=(allquestion[i][1],allquestion[i][11],allquestion[i][13], ))



dateframe=ttk.Labelframe(input_labelframe,text='Exam Date',padding=(20, 10, 10, 5))
dateframe.grid(row=1, column=9,sticky='ew',pady=10, padx=10, columnspan=4)
monthbox=ttk.Combobox(dateframe, textvariable=selectmonth, width=20)
monthbox.grid(row=0, column=1, sticky='ew',padx=3, pady=5)
monthbox['values'] = months
monthbox['state'] = 'readonly'
monthlb=ttk.Label(dateframe, text='Month')
monthlb.grid(row=0, column=0)
yearbox=ttk.Combobox(dateframe, textvariable=selectyear, width=20)
yearbox.grid(row=0, column=3, sticky='ew',padx=3, pady=5)
yearlb=ttk.Label(dateframe, text='Year')
yearlb.grid(row=0, column=2)
yearbox['values'] = years
yearbox['state'] = 'readonly'

addqframe=ttk.Labelframe(input_labelframe,text='Add selected question to test',padding=(20, 10, 10, 10))
addqframe.grid(row=3, column=5, columnspan=3, sticky='n', pady=10, padx=10)
addtotestbt=ttk.Button(addqframe, text='Add selected questions')
addtotestbt.grid(row=0, column=0, sticky='ew')
qtotestlb=ttk.Label(addqframe, text='to the test')
qtotestlb.grid(row=0, column=1, sticky='ew', padx=10)
testbox=ttk.Combobox(addqframe, textvariable=testname, width=30)
testbox.grid(row=0, column=2, sticky='ew')
testbox['values']=testnames
testbox['state']='readonly'
addqbt=ttk.Button(addqframe, text='Add questions  +', style='success.TButton')
addqbt.grid(row=0, column=8, sticky='ew', padx=10)

#commands
#------------------------------------------------ My tests tab


#sort by filter
sortfilter=('Most recently updated', 'A-Z', 'Z-A', 'Newest-Oldest', 'Oldest-Newest')
#variables
searchtestvar=tk.StringVar()
selectfilter=tk.StringVar()

#commands
def addtest():
    root.destroy()
    import addtest

def deletetest():
    x=testtreeview.selection()[0]
    DB.deleteTest(x)
    testtreeview.delete(x)

mytest_labelframe = ttk.Labelframe(mttab, text='Search test', padding=(20, 10, 10, 5))
mytest_labelframe.pack(side='top', fill='x', padx=10, pady=30)



searchtestlb= ttk.Label(mytest_labelframe, text='Search')
searchtestlb.grid(row=0, column=0, padx=3, sticky='ew')
searchtestentrybox = ttk.Entry(mytest_labelframe,textvariable=searchtestvar, width=40)
searchtestentrybox.grid(row=0, column=1, padx=3, sticky='ew', columnspan=2)

sortbylb=ttk.Label(mytest_labelframe, text='Sort by')
sortbylb.grid(row=0, column=5, padx=3, sticky='ew')
sortbybox=ttk.Combobox(mytest_labelframe, textvariable=selectfilter, width=20)
sortbybox.grid(row=0, column=6, sticky='ew',padx=3, pady=5)
sortbybox['values'] = sortfilter
sortbybox['state'] = 'readonly'


searchtestbt=ttk.Button(mytest_labelframe, text='Search tests')
searchtestbt.grid(row=0, column=7, sticky='ew', padx=15)
addtestbt=ttk.Button(mytest_labelframe, text='Add new test +',command=addtest, style='success.Outline.TButton')
addtestbt.grid(row=0, column=8, sticky='ew', padx=8)
deletetestbt=ttk.Button(mytest_labelframe, text='Delete test', command=deletetest, style='danger.Outline.TButton')
deletetestbt.grid(row=0, column=9, sticky='ew', padx=8)

testresultlb=ttk.Label(mttab, text='results:', font=('', '13'))
testresultlb.pack(padx=10, pady=10, anchor='nw')

#command
testtreeview = ttk.Treeview(mttab, style='primary.Treeview',height=10)
testtreeview.pack(fill='both',padx=10, pady=10)
testtreeview['columns'] = ('testname', 'testdescription', 'lastused')
testtreeview.column('#0', width=0, stretch=NO)
testtreeview.column('testname', width=100, anchor='center')
testtreeview.heading('#0', text='')
testtreeview.heading('testname', text='Name')
testtreeview.column('testdescription', width=150, anchor='center')
testtreeview.heading('testdescription', text='Description')
testtreeview.column('lastused', width=50, anchor='center')
testtreeview.heading('lastused', text='Last Modified')

alltest = DB.getAllTest()
for j in range (len(alltest)):
    testtreeview.insert(parent='', index='end', iid=alltest[j][0], values=(alltest[j][1],alltest[j][2] ))
def on_click(event):
    x = testtreeview.selection()[0]
    root.destroy()
    A=mytest.MyTest(x)

testtreeview.bind('<Double-1>', on_click)
#--------------------------------------------------tags tab


searchtagslb=ttk.Label(tagstab, text='Search')
searchtagslb.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
searchtagsentry=ttk.Entry(tagstab, style='info.TEntry', width=30)
searchtagsentry.grid(row=0, column=0, sticky='ew', padx=55, pady=10)
searchtagsbt=ttk.Button(tagstab, text='Search', style='info.TButton')
searchtagsbt.grid(row=0,column=1, sticky='nw', pady=10)


alltagname = DB.getAllTag()


tagstreeview = ttk.Treeview(tagstab, style='primary.Treeview',height=10)
tagstreeview.grid(row=1, column=0, sticky='ew', padx=10, columnspan=4, rowspan=20)
tagstreeview['columns'] = ('Tagname')
tagstreeview.column('#0', width=0, stretch=NO)
tagstreeview.column('Tagname', width=150, anchor='center')
tagstreeview.heading('#0', text='')
tagstreeview.heading('Tagname', text='Tag Name')

for i in range (len(alltagname)):
    tagstreeview.insert(parent='', index='end', iid=alltagname[i][0], values=(alltagname[i][1], ))

count = len(alltagname)
def addtag():
    global count
    tagname = nametag.get()
    DB.addtag(tagname)
    tagstreeview.insert(parent='', index='end', iid=count, values=(tagname, ))
    count += 1
    nametag.delete(0, 'end')

def deletetag():
    x=tagstreeview.selection()[0]
    DB.deletetag(x)
    tagstreeview.delete(x)


def edittag():
   nametag.delete(0,'end')
   selected = tagstreeview.focus()
   values = tagstreeview.item(selected, 'values')
   nametag.insert(0, values[0])


def updatetag():
    tagname=nametag.get()
    selected = tagstreeview.focus()
    tagstreeview.item(selected,text='',values=(tagname, ))
    DB.updatetag(selected, tagname)

tagsframe=ttk.Labelframe(tagstab, text='Edit tags', padding=(20, 20, 10, 10))
tagsframe.grid(row=1, column=5, sticky='ew', padx=10, columnspan=10)
nametaglb=ttk.Label(tagsframe, text='Tag')
nametaglb.grid(row=0, column=0, sticky='ew', pady=5, padx=10)
nametag=ttk.Entry(tagsframe)
nametag.grid(row=0, column=1, sticky='ew',padx=10, pady=5)
addtag=ttk.Button(tagsframe, text='add tag', command=addtag, style='success.TButton')
addtag.grid(row=1, column=0, sticky='ew',padx=10, pady=5)
deletetagbt=ttk.Button(tagsframe, text='delete selected tag', command=deletetag,style='danger.TButton')
deletetagbt.grid(row=1, column=1, sticky='ew',padx=10, pady=5)
edittagbt=ttk.Button(tagsframe, text='edit selected tag', command=edittag, style='warning.TButton')
edittagbt.grid(row=1, column=2, sticky='ew',padx=10, pady=5)
updatetagbt=ttk.Button(tagsframe, text='update tag', command=updatetag, style='primary.TButton')
updatetagbt.grid(row=1, column=3, sticky='ew',padx=10, pady=5)












root.mainloop()