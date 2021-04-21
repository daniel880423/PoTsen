from tkinter import *
root= Tk()
v1 = StringVar() #創建String型變數
Entry = Entry(root,textvariable=v1) #將變數與Entry組件綁定
Entry.pack(padx=5,pady=5)
root.mainloop()
print(v1.get())    #將輸出的內容列印

