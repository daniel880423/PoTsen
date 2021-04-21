from tkinter import *
root = Tk()
 
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
 
lb = Listbox(root, yscrollcommand=sb.set) #設置yscrollcommand選項為Scrollbar的set()方法
 
for i in range(1000):
    lb.insert(END, str(i))
 
lb.pack(side=LEFT, fill=BOTH)
 
sb.config(command=lb.yview) #設置comand參數為組件的yview()方法
 
mainloop()

