# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先導入
import tkinter.messagebox  # 要使用messagebox先要導入模組
 
# 第1步，產生實體object，建立視窗window
window = tk.Tk()
 
# 第2步，給窗口的視覺化起名字
window.title('My Window')
 
# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x
 
# 第5步，定義觸發函數功能
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')              # 提示資訊對話窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告對話窗
    # tkinter.messagebox.showerror(title='Hi', message='出錯了！')         # 提出錯誤對話窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 詢問選擇對話窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
 
# 第4步，在圖形介面上創建一個標籤用以顯示內容並放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()
 
# 第6步，主視窗迴圈顯示
window.mainloop()


