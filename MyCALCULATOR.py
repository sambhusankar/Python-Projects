from tkinter import*
root=Tk()
face=u"\u274c"

def click(event):
    
    t=event.widget.cget('text')
    if t=='C':
        entry_value.set('')
        
    elif t=='=':
        a=eval(entry_value.get())
        entry_value.set(a)
    else:
        entry_value.set(entry_value.get()+t)
    

entry_value=StringVar()
entry_value.set('')
Entry(root, textvariable=entry_value,font='Lucida 40 bold').pack(fill=X)

Label(root,text="MOTU's Calculator ♥",font='Lucida 15 bold',fg='blue').pack()


f=Frame(root,bg='grey')

b=Button(f,text='9',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f,text='8',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f,text='7',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')
b=Button(f,text='+',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left',ipadx=7)

f.pack()

f1=Frame(root,bg='grey')

b=Button(f1,text='6',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f1,text='5',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f1,text='4',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')
b=Button(f1,text='-',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left',ipadx=11)
f1.pack()

f1=Frame(root,bg='grey')

b=Button(f1,text='3',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f1,text='2',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f1,text='1',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')
b=Button(f1,text='/',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left',ipadx=11)
f1.pack()


f1=Frame(root,bg='grey')

b=Button(f1,text='.',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left',ipadx=11)

b=Button(f1,text='0',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f1,text='C',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')
b=Button(f1,text='*',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left',ipadx=7)
f1.pack()



f1=Frame(root,bg='grey')

b=Button(f1,text='00',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left',ipadx=11)

b=Button(f1,text='%',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')

b=Button(f1,text='=',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left')
b=Button(f1,text='',font='Lucida 20 bold')
b.bind('<Button-1>',click)
b.pack(side='left',ipadx=7)
f1.pack()


root.mainloop()