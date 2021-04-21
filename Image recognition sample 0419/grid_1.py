# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先導入
 
# 第1步，產生實體object，建立視窗window
window = tk.Tk()
 
# 第2步，給窗口的視覺化起名字
window.title('My Window')
 
# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x
 
# 第4步，grid 放置方法
for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
 
# 第5步，主視窗迴圈顯示
window.mainloop()
