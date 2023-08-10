# https://www.codespeedy.com/create-a-text-editor-in-python/

# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime # FN 06-08.2023

import os # FN 31-07-2023
import webbrowser # FN 07-08-2023
import re  # FN 07-08-2023

# Defining TextEditor Class
class TextEditor:

  # Defining Constructor
  def __init__(self,root):
    # Assigning root
    self.root = root
    # Title of the window
    self.root.title("TEXT EDITOR")
    # Window Geometry
    # https://www.pythontutorial.net/tkinter/tkinter-window/
    self.root.geometry("1200x700+100+100")
    # Initializing filename
    self.filename = None
    # Declaring Title variable
    self.title = StringVar()
    # Declaring Status variable
    self.status = StringVar()

    # Creating Titlebar
    self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    # Packing Titlebar to root window
    self.titlebar.pack(side=TOP,fill=BOTH)
    # Calling Settitle Function
    self.settitle()

    # Creating Statusbar
    self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    # Packing status bar to root window
    self.statusbar.pack(side=BOTTOM,fill=BOTH)
    # Initializing Status
    self.status.set("Welcome To Text Editor")

    # Creating Menubar
    self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
    # Configuring menubar on root window
    self.root.config(menu=self.menubar)

    # Creating File Menu
    self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding New file Command
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
    # Adding Open file Command
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
    # Adding Save File Command
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
    # Adding Save As file Command
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
    # Adding Seprator
    self.filemenu.add_separator()
    # Adding Exit window Command
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
    # Cascading filemenu to menubar
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding Cut text Command
    # self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut) # original
    self.editmenu.add_command(label="Cut",command=self.cut) # remove keybinding
    # Adding Copy text Command
    # self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
    self.editmenu.add_command(label="Copy",command=self.copy) # remove keybinding
    # Adding Paste text command
    # self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
    self.editmenu.add_command(label="Paste",command=self.paste) # remove keybinding
    
    
    # Adding Seprator
    self.editmenu.add_separator()
    # Adding Undo text Command
    self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
    # Cascading editmenu to menubar
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding About Command
    self.helpmenu.add_command(label="About",command=self.infoabout)
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)


    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    # Creating Text Area
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
    # Packing scrollbar to root window
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbar to text area
    scrol_y.config(command=self.txtarea.yview)
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)

####### FN 2023-07-31

    # Creating Predicates menu
    self.predicatesMenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding commands
    # self.predicatesMenu.add_command(label="derivedFrom",command=self.insDerivedFrom)  # old version

    self.predicatesMenu.add_command(label="derivedFrom", command=lambda : self.insPredicate("anota:derivedFrom"))
    self.predicatesMenu.add_command(label="references", command=lambda : self.insPredicate("anota:references"))
    self.predicatesMenu.add_command(label="screenShot", command=lambda : self.insPredicate("anota:screenShot"))
    self.predicatesMenu.add_command(label="localCopy", command=lambda : self.insLocalCopy("anota:localCopy"))
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Predicates", menu=self.predicatesMenu)


    # Creating Tags menu
    self.tagsMenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    tagList=os.listdir ("../Diario/Tags") # seria bom testar se o diretório existe e tomar a ação cabível
    # Adding commands
    for tag in tagList :
        self.tagsMenu.add_command(label=tag, command=lambda tg = tag : self.insTag(tg)) # https://stackoverflow.com/questions/74290187/get-selected-option-from-menu-tkinter

    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Tags", menu=self.tagsMenu)
    
    # Set text modified events
    # https://www.tutorialspoint.com/list-of-all-tkinter-events
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/event-types.html
    self.txtarea.bind('<Button>', self.textModified)
    self.txtarea.bind('<KeyPress>', self.textModified)

#######

####### FN 2023-08-07

    # Creating Utils menu
    self.utilsMenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding commands
    # self.predicatesMenu.add_command(label="derivedFrom",command=self.insDerivedFrom)  # old version

    self.utilsMenu.add_command(label="open all URLs", command= self.openAllURLs)
    #self.utilsMenu.add_command(label="references", command=lambda : self.insPredicate("anota:references"))
    #self.utilsMenu.add_command(label="screenShot", command=lambda : self.insPredicate("anota:screenShot"))
    #self.utils.add_command(label="localCopy", command=lambda : self.insLocalCopy("anota:localCopy"))
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Utils", menu=self.utilsMenu)

#######

    # Calling shortcuts funtion
    self.shortcuts()

####### FN 2023-07-29
  # Defining settitle function
  def insDerivedFrom(self):
	# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/text-index.html
    self.txtarea.insert('insert', "[anota:derivedFrom]()")
    # https://stackoverflow.com/questions/63708507/how-to-move-the-insertion-cursor-of-a-tkinter-text-widget-to-a-certain-index
    self.txtarea.mark_set('insert', 'insert-1c')
#######

####### FN 2023-07-31
  # Defining settitle function
  
  def insPredicate(self, pred):
    self.txtarea.insert('insert', "[")
    self.txtarea.insert('insert', pred)
    self.txtarea.insert('insert', "](")
    # https://www.tutorialspoint.com/copy-from-clipboard-using-python-and-tkinter
    cliptext=self.txtarea.clipboard_get()
    matchStart=cliptext.find("/Anota/Diario/")
    if (matchStart>=0) :
        cliptext=cliptext[(matchStart+14):]
    self.txtarea.insert('insert', cliptext)
    self.txtarea.insert('insert', ")")

  def insLocalCopy(self, pred):
    self.txtarea.insert('insert', "[")
    self.txtarea.insert('insert', pred)
    self.txtarea.insert('insert', "](..")
    # https://www.tutorialspoint.com/copy-from-clipboard-using-python-and-tkinter
    cliptext=self.txtarea.clipboard_get()
    matchStart=cliptext.find("/Anota/Artigos/")
    if (matchStart>=0) :
        cliptext=cliptext[(matchStart+6):]
    self.txtarea.insert('insert', cliptext)
    self.txtarea.insert('insert', ")")

  def insTag(self, tg):
    self.txtarea.insert('insert', "[anota:hasTag ")
    self.txtarea.insert('insert', tg)
    self.txtarea.insert('insert', "](Tags/")
    # https://www.tutorialspoint.com/copy-from-clipboard-using-python-and-tkinter
    self.txtarea.insert('insert', tg)
    self.txtarea.insert('insert', ")")

  def textModified(self, ev):
    # https://www.tutorialspoint.com/list-of-all-tkinter-events
    self.status.set("text modified")

#######

####### FN 2023-08-07

  def checkURL(self, str):
# https://www.tutorialspoint.com/python-program-to-check-for-url-in-a-string
# findall() function used with the conditions which is valid for url in the strings
# The regex function can store all the characters including the upper case and the lower case of the alphabets, numbers, special cases and characters etc 8. Python program to check for url in a string
    regex= 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' 
    URL= re.findall(regex,str) 
    return URL 

  def openAllURLs(self):
    # Reading the data from text area
    data = self.txtarea.get("1.0",END)
    webbrowser.open_new('../Diario/') # https://docs.python.org/3/library/webbrowser.html
    urls=self.checkURL(data)
    for url in urls :
      webbrowser.open_new_tab(url)

##########

  # Defining settitle function
  def settitle(self):
    # Checking if Filename is not None
    if self.filename:
      # Updating Title as filename
      self.title.set(self.filename)
    else:
      # Updating Title as Untitled
      self.title.set("Untitled")

  # Defining New file Function
  def newfile(self,*args):
    # Clearing the Text Area
    self.txtarea.delete("1.0",END)
    # Updating filename as None
    self.filename = None
    # Calling settitle funtion
    self.settitle()
    # updating status
    self.status.set("New File Created")

  # Defining Open File Funtion
  def openfile(self,*args):
    # Exception handling
    try:
      # Asking for file to open
      self.filename = filedialog.askopenfilename(title = "Select file",initialdir = "../Diario",filetypes = (("All Files","*.*"),("Markdown Files","*.md"),("Text Files","*.txt"),("Python Files","*.py")))
      # checking if filename not none
      if self.filename:
        # opening file in readmode
        infile = open(self.filename,"r", encoding="utf-8")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing the file  
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save File Funtion
  def savefile(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Reading the data from text area
        data = self.txtarea.get("1.0",END)
        # opening File in write mode
        outfile = open(self.filename,"w", encoding="utf-8")
        # Writing Data into file
        outfile.write(data)
        # Closing File
        outfile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Saved Successfully")
      else:
        self.saveasfile()
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save As File Funtion
  def saveasfile(self,*args):
    # Exception handling
    try:
      # build default filename
      current_date = datetime.now()
      initFileName = current_date.strftime('%Y-%m-%dT%H%M%S.md') # https://www.tutorialspoint.com/How-do-I-get-an-ISO-8601-date-in-string-format-in-Python
      # Asking for file name and type to save
      # https://www.geeksforgeeks.org/how-to-specify-the-file-path-in-a-tkinter-filedialog/
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".md",initialdir = "../Diario",initialfile = initFileName,filetypes = (("All Files","*.*"),("Markdown Files","*.md"),("Text Files","*.txt"),("Python Files","*.py")))
      # Reading the data from text area
      data = self.txtarea.get("1.0",END)
      # opening File in write mode
      outfile = open(untitledfile,"w", encoding="utf-8")
      # Writing Data into file
      outfile.write(data)
      # Closing File
      outfile.close()
      # Updating filename as Untitled
      self.filename = untitledfile
      # Calling Set title
      self.settitle()
      # Updating Status
      self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Exit Funtion
  def exit(self,*args):
    op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
    if op>0:
      self.root.destroy()
    else:
      return

  # Defining Cut Funtion
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")

  # Defining Copy Funtion
  def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")

  # Defining Paste Funtion
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")

  # Defining Undo Funtion
  def undo(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # opening File in read mode
        infile = open(self.filename,"r")
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing File
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining About Funtion
  def infoabout(self):
    messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python.")

  # Defining shortcuts Funtion
  def shortcuts(self):
    # Binding Ctrl+n to newfile funtion
    self.txtarea.bind("<Control-n>",self.newfile)
    # Binding Ctrl+o to openfile funtion
    self.txtarea.bind("<Control-o>",self.openfile)
    # Binding Ctrl+s to savefile funtion
    self.txtarea.bind("<Control-s>",self.savefile)
    # Binding Ctrl+a to saveasfile funtion
    self.txtarea.bind("<Control-a>",self.saveasfile)
    # Binding Ctrl+e to exit funtion
    self.txtarea.bind("<Control-e>",self.exit)
    # Binding Ctrl+x to cut funtion
    # self.txtarea.bind("<Control-x>",self.cut)  # commented out FN 07.08.2023
    # Binding Ctrl+c to copy funtion
    # self.txtarea.bind("<Control-c>",self.copy)
    # Binding Ctrl+v to paste funtion
    # self.txtarea.bind("<Control-v>",self.paste)
    # Binding Ctrl+u to undo funtion
    self.txtarea.bind("<Control-u>",self.undo)

# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()
