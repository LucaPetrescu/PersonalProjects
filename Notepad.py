from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile,asksaveasfilename

win = Tk()
win.title("Notepad")

def open_file():
    blank.delete("1.0", END)
    file = askopenfile(mode='r', filetypes=[('rext files','*.txt')])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)

def save_file():
    notepad_text = blank.get("1.0", "end-lc")
    file = asksaveasfilename(title='Saves', filetypes=[('text files', '*.txt')])
    with open(file, "w") as data:
        data.write(notepad_text)

menubar = Menu(win)
win.config(menu = menubar)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_command(label = "Exit", command = win.destroy)

blank = Text(win, font=("arial", 10))
blank.pack()

win.mainloop()
