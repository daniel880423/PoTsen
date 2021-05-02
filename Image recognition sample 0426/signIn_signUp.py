
from tkinter import *
 
root = Tk()
 
Label(root, text="帳號").grid(row=0, sticky=W)
Label(root, text="密碼").grid(row=1, sticky=W)
 
user = Entry(root)
user.grid(row=0, column=1)

passwd = Entry(root, show="*")
passwd.grid(row=1, column=1)
 
photo = PhotoImage(file="account.png")
photo1 = PhotoImage(file="image_file.gif")
photo2 = PhotoImage(file="android.png")

showPhoto = Label(root, image=photo)
showPhoto.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

def signIn():
    if user.get()=="alvin":
        if passwd.get()=="123456":
            showPhoto.configure(image=photo1)
        else:
            messagebox.showinfo(title='登入錯誤', message='密碼有誤')              # 提示資訊對話窗
    elif user.get()=="mary":
        if passwd.get()=="654321":
            showPhoto.configure(image=photo2)
        else:
            messagebox.showinfo(title='登入錯誤', message='密碼有誤')   
    else:
        messagebox.showinfo(title='登入錯誤', message='無此帳號')              # 提示資訊對話窗

def signUp():
    pass

 
Button(text="登入", width=10, command=signIn).grid(row=2, columnspan=3, pady=5)
Button(text="註冊", width=10, command=signUp).grid(row=3, columnspan=6, pady=5)
 
mainloop()

