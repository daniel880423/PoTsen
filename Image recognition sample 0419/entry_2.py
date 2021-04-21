from tkinter import *
 
def func1():
    if e1.get() == "admin":
        print('名稱合法')
        return True
    else:
        return False
def func2():
    print("請重新輸入")
    e1.delete(0,END)
    return True
 
root = Tk()
root.title("示例")
Label(root,text="用戶名").grid(row=0)
Label(root,text="密碼").grid(row=1)
#當用戶框失去焦點時驗證
e1 = Entry(root,validate="focusout",validatecommand=func1,invalidcommand=func2) 
e2 = Entry(root,show="*")
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
 
mainloop()

