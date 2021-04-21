from tkinter import *
root= Tk()
v1 = StringVar()    #創建string型變數
v1.set('hello')     #給變數賦初始值
Entry = Entry(root,textvariable=v1) #將變數與Entry組件綁定
Entry.pack(padx=5,pady=5)
root.mainloop()

