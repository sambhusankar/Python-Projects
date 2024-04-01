from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
root=Tk()

def newfile():
    text.delete(1.0,END)
    
def openfile():
    global file 
    text.delete(1.0,END)
    file=askopenfilename()
    f=open(file,'r')
    
    text.insert(1.0,f.read())
    f.close()
def savefile():
    global file
    file=asksaveasfilename()
    f2=open(file,'w')
    data=f2.write(text.get(1.0,END))
    f2.close()
    
def cut():
    text.event_generate("<>")
    
def copy():
    text.event_generate("<>")
def paste():
    text.event_generate("<>")
def about():
    messagebox.showinfo("",'notepad by sankar')
    
scroll=Scrollbar(root)
scroll.pack(side='right',fill='y')
text=Text(root,font='Lucida 20', yscrollcommand=scroll.set)
text.pack()
menubar=Menu(root)
filemenu=Menu(menubar)


filemenu.add_command(label='new file',command=newfile)

filemenu.add_command(label='open file',command=openfile)
filemenu.add_command(label='save file',command=savefile)
menubar.add_cascade(label='file',menu=filemenu)





editmenu=Menu(menubar)


editmenu.add_command(label='cut',command=cut)

editmenu.add_command(label='copy',command=copy)
editmenu.add_command(label='paste',command=paste)
menubar.add_cascade(label='Edit',menu=editmenu)



helpmenu=Menu(menubar)

helpmenu.add_command(label='about notepad',command=about)

menubar.add_cascade(label='help',menu=helpmenu)


root.config(menu=menubar)






root.mainloop()