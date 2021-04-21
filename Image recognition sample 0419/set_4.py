from tkinter import *
root= Tk()
v1 = IntVar()
v1.set('hello')
Entry = Entry(root,textvariable=v1)
Entry.pack(padx=5,pady=5)
root.mainloop()
print(v1.get())