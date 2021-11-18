# from ttkbootstrap import Style
# from tkinter import ttk
#
#
# style = Style()
#
# window = style.master
# ttk.Label(window, text='My widgets',style='secondary.TLabel', font='Opensans 30').pack(side='top')
# ttk.Button(window, text="Submit", style='success.TButton').pack(side='left', padx=5, pady=10)
# ttk.Button(window, text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)
# ttk.Entry(window, style='secondary.TEntry').pack(side='bottom', padx=5, pady=10)
# window.mainloop()



# from ttkbootstrap import Style
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.title("Tab Widget")
# tabControl = ttk.Notebook(root, style='custom.TNotebook')
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
# tabControl.pack(anchor='center')
#
#
# tabControl.add(tab1, text='Tab 1')
# tabControl.add(tab2, text='Tab 2')
#
# root.mainloop()

# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# style = ttk.Style()
# style.theme_create( "MyStyle", parent="alt", settings={
#         "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
#         "TNotebook.Tab": {"configure": {"padding": [10, 10] },}})
#
# style.theme_use("MyStyle")
#
# a_notebook = ttk.Notebook(root, width=200, height=200)
# a_tab = ttk.Frame(a_notebook)
# a_notebook.add(a_tab, text = 'This is the first tab')
# another_tab = ttk.Frame(a_notebook)
# a_notebook.add(another_tab, text = 'This is another tab')
# a_notebook.pack(expand=True, fill=tk.BOTH)
#
# tk.Button(root, text='Some Text!').pack(fill=tk.X)
#
# root.mainloop()
# # create a notebook
# notebook = ttk.Notebook(root, style='TNotebook')
# notebook.pack(tabposition='wn', pady=10, expand=True)
#
# # create frames
# frame1 = ttk.Frame(notebook, width=400, height=280)
# frame2 = ttk.Frame(notebook, width=400, height=280)
#
# frame1.pack(fill='both', expand=True)
# frame2.pack(fill='both', expand=True)
#
# # add frames to notebook
#
# notebook.add(frame1, text='General Information')
# notebook.add(frame2, text='Profile')
#
#
# root.mainloop()
import tkinter
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# import tkinter
# from tkinter import ttk
# import tkinter as tk
# from ttkbootstrap import Style
# cf=tk.Tk()
# style = Style()
#
#
# group1 = ttk.Frame(cf, padding=10)
# for x in range(5):
#     ttk.Checkbutton(group1, text=f'Option {x+1}').pack(fill='x')
# cf.add(group1, title='Option Group 1', style='primary.TButton')
#
# group2 = ttk.Frame(cf, padding=10)
# for x in range(5):
#     ttk.Checkbutton(group2, text=f'Option {x+1}').pack(fill='x')
# cf.add(group2, title='Option Group 2', style='danger.TButton')
#
# group3 = ttk.Frame(cf, padding=10)
# for x in range(5):
#     ttk.Checkbutton(group3, text=f'Option {x+1}').pack(fill='x')
# cf.add(group3, title='Option Group 3', style='success.TButton')
#



#
# cf.mainloop()

# from ttkwidgets import CheckboxTreeview
# import tkinter as tk
#
# root = tk.Tk()
# #
# tree = CheckboxTreeview(root)
# tree.pack()
#
# tree.insert("", "end", "1", text="1")
# tree.insert("1", "end", "11", text="11")
# tree.insert("1", "end", "12", text="12")
# tree.insert("11", "end", "111", text="111")
# tree.insert("", "end", "2", text="2")
# #
# root.mainloop()
# import tkinter
# from tkinter import ttk
# from ttkbootstrap import Style
#
# class Application(tkinter.Tk):
#
#     def __init__(self):
#         super().__init__()
#         self.title('Collapsing Frame')
#         self.style = Style()
#
#         cf = CollapsingFrame(self)
#         cf.pack(fill='both')
#
#         # option group 1
#         group1 = ttk.Frame(cf, padding=10)
#         for x in range(5):
#             ttk.Checkbutton(group1, text=f'Option {x + 1}').pack(fill='x')
#         cf.add(group1, title='Option Group 1', style='primary.TButton')
#
#         # option group 2
#         group2 = ttk.Frame(cf, padding=10)
#         for x in range(5):
#             ttk.Checkbutton(group2, text=f'Option {x + 1}').pack(fill='x')
#         cf.add(group2, title='Option Group 2', style='danger.TButton')
#
#         # option group 3
#         group3 = ttk.Frame(cf, padding=10)
#         for x in range(5):
#             ttk.Checkbutton(group3, text=f'Option {x + 1}').pack(fill='x')
#         cf.add(group3, title='Option Group 3', style='success.TButton')
#
#
# class CollapsingFrame(ttk.Frame):
#     """
#     A collapsible frame widget that opens and closes with a button click.
#     """
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.columnconfigure(0, weight=1)
#         self.cumulative_rows = 0
#         # self.images = [tkinter.PhotoImage(name='open', file='icons8-double-up-24.png'),
#         #                tkinter.PhotoImage(name='closed', file='icons8-double-right-24.png')]
#
#     def add(self, child, title="", style='primary.TButton', **kwargs):
#         """Add a child to the collapsible frame
#
#         :param ttk.Frame child: the child frame to add to the widget
#         :param str title: the title appearing on the collapsible section header
#         :param str style: the ttk style to apply to the collapsible section header
#         """
#         if child.winfo_class() != 'TFrame':  # must be a frame
#             return
#         style_color = style.split('.')[0]
#         frm = ttk.Frame(self, style=f'{style_color}.TFrame')
#         frm.grid(row=self.cumulative_rows, column=0, sticky='ew')
#
#         # header title
#         lbl = ttk.Label(frm, text=title, style=f'{style_color}.Invert.TLabel')
#         if kwargs.get('textvariable'):
#             lbl.configure(textvariable=kwargs.get('textvariable'))
#         lbl.pack(side='left', fill='both', padx=10)
#
#         # header toggle button
#         btn = ttk.Button(frm, style=style, command=lambda c=child: self._toggle_open_close(child))
#         btn.pack(side='right')
#
#         # assign toggle button to child so that it's accesible when toggling (need to change image)
#         child.btn = btn
#         child.grid(row=self.cumulative_rows + 1, column=0, sticky='news')
#
#         # increment the row assignment
#         self.cumulative_rows += 2
#
#     def _toggle_open_close(self, child):
#         """
#         Open or close the section and change the toggle button image accordingly
#
#         :param ttk.Frame child: the child element to add or remove from grid manager
#         """
#         if child.winfo_viewable():
#             child.grid_remove()
#             child.btn.configure(image='closed')
#         else:
#             child.grid()
#             child.btn.configure(image='open')
#
#
# if __name__ == '__main__':
#     Application().mainloop()
# from ttkwidgets import CheckboxTreeview
# import tkinter as tk
# root = tk.Tk()
# topics = ['1:Stoichiometric Relationships', '2:Atomic Structure', '3:Periodicity',
#           '4:Chemical Bonding and Structure', '5:Energetics/Thermochemistry',
#           '6:Chemical Kinetics', '7:Equilibrium', '8:Acids and Bases', '9:Redox Processes',
#           '10:Organic Chemistry', '11:Measurement and Data Processing', '12:Atomic Structure (HL)',
#           '13:The Periodic Table (HL)', '14:Chemical Bonding and Structure (HL)',
#           '15:Energetics/Thermochemistry (HL)', '16:Chemical Kinetics (HL)', '17 Equilibrium (HL)',
#           '18:Acids and Bases (HL)', '19:Redox Processes (HL)','20:Organic Chemistry (HL)',
#           '21:Measurement and Analysis (HL)']
# suptopics=[['1.1:Introduction to the particulate nature of matter and chemical change',
#             '1.2:The mole concept','1.3: Reacting masses and volumes'],['2.1:The nuclear atom',
#             '2.2:Electron configuration'],['3.1:Periodic table','3.2:Periodic trends'],
#            ['4.1:Ionic bonding and structure','4.2:Covalent bonding','4.3:Covalent structures',
#             '4.4:Intermolecular forces','4.5:Metallic bonding'],['5.1:Measuring energy changes',
#             '5.2:Hess’s Law','5.3:Bond enthalpies'],['6.1:Collision theory and rates of reaction'],
#            ['7.1:Equilibrium'], ['8.1:Theories of acids and bases','8.2:Properties of acids and bases',
#             '8.3:The pH scale', '8.4:Strong and weak acids and bases','8.5:Acid deposition'],
#             ['9.1:Oxidation and reduction','9.2:Electrochemical cells'],['10.1:Fundamentals of organic chemistry',
#             '10.2:Functional group chemistry'],['11.1:Uncertainties and errors in measurement and results',
#             '11.2:Graphical techniques','11.3:Spectroscopic identification of organic compounds'],
#             ['12.1:Electrons in atoms'],['13.1:First-row d-block elements','13.2:Coloured complexes'],
#            ['14.1:Covalent bonding and electron domain and molecular geometries','14.2:Hybridization'],
#            ['15.1:Energy cycles','15.2:Entropy and spontaneity'],['16.1:Rate expression and reaction mechanism',
#             '16.2:Activation energy'],['17.1:The equilibrium law'],['18.1:Lewis acids and bases',
#             '18.2:Calculations involving acids and bases','18.3:pH curves'],['19.1:Electrochemical cells'],
#             ['20.1:Types of organic reactions','20.2:Synthetic routes','20.3:Stereoisomerism'],
#            ['21.1:Spectroscopic identification of organic compounds']]
#
# #read subtopic file
# tempsubtopic=[]
# with open('Chem_SubTopics.txt') as f:
#     line=f.readlines()
#     for lines in line:
#         #remove newline or spacebar
#         lines=lines.strip()
#         tempsubtopic.append(lines)
#         f.close()
# counter=0
# arr_subtopic=[]
# subtopic=[]
#
# for i in range (0,len(tempsubtopic)):
#     #assign number
#     subnumber=tempsubtopic[i].split('.')
#     topicnumber=topics[counter].split(':')
#     if subnumber[0]==topicnumber[0]:
#         arr_subtopic.append(tempsubtopic)
#     else:
#         #print(arr_subtopic)
#         subtopic.append(arr_subtopic)
#         arr_subtopic=[]
#         arr_subtopic.append(tempsubtopic[i])
#         counter=counter+1
#         if i==(len(tempsubtopic)-1):
#             subtopic.append(arr_subtopic)
# checkbox=dict()
# for i in range(0,len(topics)):
#        checkbox[topics[i]] = subtopic[i]
# key_list = list(checkbox.keys())
# value_list = list(checkbox.values())
#
# topiccheckbox=dict()
# for i in range(len(topics)):
#     topiccheckbox[topics[i]]=suptopics[i]
# print(topiccheckbox)
# #CheckboxTreeview
# tree = CheckboxTreeview(root)
# tree.pack()
# id = 22
# for i in range(0,len(topics)):
#     #Assign Topic
#     tree.insert("", "end", i, text=key_list[i])
#     for j in range(0,len(value_list[i])):
#         tree.insert(i, "end", id, text=value_list[i][j])
#         id = id + 1
# root.mainloop()

from Tkinter import *



def addBox():
    labelframe = Tkinter.Frame()
    labelframe.bind("<Add Input>", callback)
    labelframe.pack()

labelframe = Tkinter.Frame()

labelFrom = Tkinter.Label(labelframe, text= "from")
labelFrom.grid(column=1, row=0)
e = Tkinter.Entry(labelframe)
e.grid(column=1, row=1)

labelTo = Tkinter.Label(labelframe, text= "to")
labelTo.grid(column=2, row=0)
e2 = Tkinter.Entry(labelframe)
e2.grid(column=2, row=1)

labelframe.pack()

addboxButton = Button( root,text='<Add Time Input>', fg="Red",command="addBox")
addboxButton.pack(side=Tkinter.TOP)
