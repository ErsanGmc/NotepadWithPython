import tkinter
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showinfo

class Notepad:
    __root=Tk()
    __thisWidth=800 # Pencere genişliği değiştirildi
    __thisHeight=600
    __thisTextArea=Text(__root, font=("Helvetica", 12)) # Yazı tipi değiştirildi
    __thisMenuBar=Menu(__root, font=("Helvetica", 12), bg="white", fg="black", activebackground="gray", activeforeground="white")
    __thisFileMenu=Menu(__thisMenuBar,tearoff=0, font=("Helvetica", 12), bg="white", fg="black", activebackground="gray", activeforeground="white")
    __thisEditMenu=Menu(__thisMenuBar,tearoff=0, font=("Helvetica", 12), bg="white", fg="black", activebackground="gray", activeforeground="white")
    __thisHelpMenu=Menu(__thisMenuBar,tearoff=0, font=("Helvetica", 12), bg="white", fg="black", activebackground="gray", activeforeground="white")    
    __thisScrollBar=Scrollbar(__thisTextArea)
    __file=None
    def __init__(self,**kwargs):
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass
        try:
            self.__thisWidth=kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight=kwargs['height']
        except KeyError:
            pass
        self.__root.title("Untilted-Notepad")
        screenWidth=self.__root.winfo_screenmmwidth()
        screenHeight=self.__root.winfo_screenmmheight()

        left=(screenWidth/2)-(self.__thisWidth/2)
        top=(screenHeight/2)-(self.__thisHeight/2)

        self.__root.geometry('%dx%d+%d+%d'%(self.__thisWidth,self.__thisHeight,left,top))

        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        self.__thisTextArea.grid(sticky=N+E+S+W)
        self.__thisFileMenu.add_command(label="New",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)


        self.__thisEditMenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.__cut)
        self.__root.bind("<Control-x>", self.__cut)
        self.__thisEditMenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.__copy)
        self.__root.bind("<Control-c>", self.__copy)
        self.__thisEditMenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.__paste)
        self.__root.bind("<Control-v>", self.__paste)
        self.__thisEditMenu.add_command(label="Undo",accelerator="Ctrl+Z", command=self.__undo)
        self.__root.bind("<Control-<>", self.__undo)

        self.__thisMenuBar.add_cascade(label="Edit",menu=self.__thisEditMenu)

        # Format menu
        self.__thisFormatMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisMenuBar.add_cascade(label="Format", menu=self.__thisFormatMenu)

        # Font boyutunu ayarla
        self.__fontSizeVar = IntVar()
        self.__fontSizeVar.set(12)  # varsayılan olarak 12 punto ayarla
        self.__thisFormatMenu.add_radiobutton(label="Font Size", variable=self.__fontSizeVar, value=12, command=self.__setFont)

         # Font stili
        self.__fontStyleVar = StringVar()
        self.__fontStyleVar.set('normal')  # varsayılan olarak normal stil ayarla
        self.__thisFormatMenu.add_radiobutton(label="Normal", variable=self.__fontStyleVar, value='normal', command=self.__setFont)
        self.__thisFormatMenu.add_radiobutton(label="Bold", variable=self.__fontStyleVar, value='bold', command=self.__setFont)
        self.__thisFormatMenu.add_radiobutton(label="Italic", variable=self.__fontStyleVar, value='italic', command=self.__setFont)

        self.__thisHelpMenu.add_command(label="About Notepad",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)

        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
     self.__root.destroy()

    def __showAbout(self):
        showinfo("Notepad","Tatsumaki")

    def __openFile(self):
        self.__file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file=="":
                self.__file=None
        else:
            self.__root.title(os.path.basename(self.__file)+"-Notepad")
            self.__thisTextArea.delete(1.0,END)
            file=open(self.__file,"r")
            self.__thisTextArea.insert(1.0,file.read())
            file.close()       
    def __newFile(self):
        self.__root.title("Untiteled-Notepad")
        self.__file=None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):
        if self.__file==None:
            self.__file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file=="":
                self.__file=None
            else:
                file=open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()

                self.__root.title(os.path.basename(self.__file)+"-Notepad")
                
        else:
            file=open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
    
    def __undo(self):
        self.__thisTextArea.edit_undo()

    def __setFont(self):
        font = f"TkDefaultFont {self.__fontSizeVar.get()} {self.__fontStyleVar.get()}"
        self.__thisTextArea.configure(font=font)

    def run(self):
        self.__root.mainloop()    

notepad=Notepad(width=600,height=400)
notepad.run()