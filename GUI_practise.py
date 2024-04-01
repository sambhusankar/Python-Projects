from tkinter import*
root=Tk()
root.title('sankar')
root.configure(background='grey')
def update():
    
    import time
   
    time.sleep(2)
    svar.set('working...')
    

canva=Canvas(root,width=300, height=300)
canva.pack()

canva.create_line(500,5000,150,30,fill='red')
canva.create_rectangle(5,4,40,30)

butt=Button(canva,text='press',command=update)
butt.pack()

#butt.bind('<Button-1>',sankar)

var=StringVar()
radio=Radiobutton(root,text='sankar',value='Sankar').pack()

en=StringVar()
a=Entry(root, textvariable=en).pack()

scroll=Scrollbar(root)
scroll.pack(side='left',fill=Y)

l=Listbox(root,yscrollcommand=scroll.set)
#while True:
for I in range(100):
    l.insert(END,I)
    l.pack()
    
text=Text(root, yscrollcommand=scroll.set).pack()

#scroll.config(command=l.yview)
svar=StringVar()
svar.set('Ready')
lab=Label(root, textvariable=svar,bg='red',anchor='w').pack(side='bottom',fill='x')



root.mainloop()