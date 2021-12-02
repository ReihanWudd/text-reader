from tkinter import *
from tkinter import filedialog as fd


root = Tk()
root.title("menu")
root.geometry("400x400")

def buka():
    new = Toplevel()
def bukafile():
    tipe = ("txt file","*.txt"),("python file","*.py"),("all file","*.*")
    filenama = fd.askopenfilename(filetypes=tipe)
    filenama2 = open(filenama,"r")
    tulisan.insert("1.0",filenama2.read())

jdl = Label(root,text="INSERT YOUR TEXT").grid()
tulisan = Text(root,height=10)
tulisan.grid(padx=10,pady = 5)

menunya = Menu(root)
mn = Menu(menunya,tearoff=0)
menunya.add_cascade(label="file",menu=mn)
mn.add_command(label="new..",command=buka)
mn.add_command(label="open",command=bukafile)
mn.add_separator()
mn.add_command(label="exit",command=root.destroy)

mn2 = Menu(menunya,tearoff=0)
menunya.add_cascade(label="edit",menu=mn2)
mn2.add_command(label="color...",command=buka)
mn2.add_command(label="frame",command=bukafile)
mn2.add_separator()
mn2.add_command(label="extention",command=root.destroy)

mn3 = Menu(menunya,tearoff=0)
menunya.add_cascade(label="help",menu=mn3)
mn3.add_command(label="about",command=buka)
mn3.add_command(label="profile",command=bukafile)



root.config(menu=menunya)
root.mainloop()