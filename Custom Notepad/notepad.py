import tkinter
import os 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.colorchooser import askcolor
from tkinter import font as tkFont

class Notepad:
    __root = Tk()
    __thisWidth = 900
    __thisHeight = 900
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0, background="#3a3e3f", foreground="white")
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0, background="#3a3e3f", foreground="white")
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0, background="#3a3e3f", foreground="white")
    __thisFontMenu = Menu(__thisMenuBar, tearoff=0, background="#3a3e3f", foreground="white")
    __thisScrollBar = Scrollbar(__thisTextArea)	 
    __file = None

    def __init__(self, **kwargs):
        self.__font = tkFont.Font(family="Arial", size=12)
        self.__font_color = "black"

        #self.__navbar = Frame(self.__root, bg="#3a3e3f", width=50)
        #self.__navbar.pack(side=LEFT, fill=Y)

        #button_font_color = Button(self.__navbar,text="Font Color",command=self.__changeFontColor)
        #button_font_color.pack(pady=10)

        #button_bg_color = Button(self.__navbar, text="Background Color", command=self.__changeBgColor)
        #button_bg_color.pack(pady=10)

        #button_change_font = Button(self.__navbar, text="Change Font", command=self.__changeFont)
        #button_change_font.pack(pady=10)

        # Uncomment the following lines if you want to include a custom button
        # button_custom = Button(self.__navbar, text="Custom Button", command=self.__customFunction)
        # button_custom.pack(pady=10)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title("Untitled - Notepad")

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2) 
        top = (screenHeight / 2) - (self.__thisHeight /2) 

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top)) 
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky=N + E + S + W)
        self.__thisFontMenu.add_command(label="Background Color", command=self.__changeBgColor)
        self.__thisFontMenu.add_command(label="Font Color",command=self.__changeFontColor)
        self.__thisFontMenu.add_command(label="Font Size",command=self.__changeFontSize)
        self.__thisMenuBar.add_cascade(label="Style",menu=self.__thisFontMenu)
        self.__thisFileMenu.add_command(label="New File", command=self.__newFile) 
        self.__thisFileMenu.add_command(label="Open File", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save File", command=self.__saveFile) 
        self.__thisFileMenu.add_separator()										 
        self.__thisFileMenu.add_command(label="Exit Mynotes", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)	 
        
        self.__thisEditMenu.add_command(label="Cut Text", command=self.__cut)			 
        self.__thisEditMenu.add_command(label="Copy Text", command=self.__copy)		 
        self.__thisEditMenu.add_command(label="Paste Text", command=self.__paste)		 
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)	 
        
        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)				 
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __changeFontSize(self):
        input=int(Entry(self.__root))
        input.pack()
        print(input)

   
    def __changeFontColor(self):
        color = askcolor(title="Choose Font Color", color=self.__font_color)
        if color:
            self.__font_color = color[1]
            self.__thisTextArea.configure(fg=self.__font_color)

    def __changeBgColor(self):
        color = askcolor(title="Choose Background Color", color=self.__thisTextArea.cget("bg"))
        if color:
            self.__thisTextArea.configure(background=color[1])		

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo(title="MyNotes", message="Pranjal Prakarsh")

    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt"),
                                            ("Rich Text Format", "*.rtf")])

        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - MyNotes")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    def __newFile(self):
        self.__root.title("Untitled - MyNotes")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__file is None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                        ("Text Documents", "*.txt"),
                                                        ("Rich Text Format", "*.rtf")])

            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - MyNotes")
        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __customFunction(self):
        # Placeholder for custom functionality
        print("Custom functionality triggered!")

    def run(self):
        self.__root.mainloop()

# Run main application
notepad = Notepad(width=600, height=400)
notepad.run()
