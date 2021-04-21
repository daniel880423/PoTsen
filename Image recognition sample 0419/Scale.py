# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先導入
 
# 第1步，產生實體object，建立視窗window
window = tk.Tk()
 
# 第2步，給窗口的視覺化起名字
window.title('My Window')
 
# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x
 
# 第4步，在圖形介面上創建一個標籤label用以顯示並放置
l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l.pack()
 
# 第6步，定義一個觸發函數功能
def print_selection(v):
    l.config(text='you have selected ' + v)
# 第5步，創建一個尺度滑條，長度200字元，從0開始10結束，以2為刻度，精度為0.01，觸發調用print_selection函數
s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
 
# 第7步，主視窗迴圈顯示
window.mainloop()

