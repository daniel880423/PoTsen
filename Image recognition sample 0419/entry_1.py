# -*- coding: utf-8 -*-

import tkinter as tk # 使用Tkinter前需要先導入
# 第1步，產生實體object，建立視窗window
window = tk.Tk()

# 第2步，給窗口的視覺化起名字
window.title('My Window')

# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300') # 這裡的乘是小x

# 第4步，在圖形介面上設定輸入框控制項entry並放置控制項
e1 = tk.Entry(window, show='*', font=('Arial', 14)) # 顯示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14)) # 顯示成明文形式
e1.pack()
e2.pack()

# 第5步，主視窗迴圈顯示
window.mainloop()

