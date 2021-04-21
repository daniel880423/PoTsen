from tkinter import *
 
def func1(act,index,content,old_content,validate,reason,name):
    if e1.get() == "admin":
        print('名稱合法')
        print(act,index,content,old_content,validate,reason,name)
        return True
    else:
        print('請重新輸入')
        print(act,index,content,old_content,validate,reason,name)
        return False
root = Tk()
root.title("示例")
Label(root,text="用戶名").grid(row=0)
Label(root,text="密碼").grid(row=1)
test = root.register(func1)
e1 = Entry(root,validate="focusout",validatecommand=(test,"%d","%i",'%P','%s','%v','%V','%W'))
e2 = Entry(root,show="*")
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
 
mainloop()
