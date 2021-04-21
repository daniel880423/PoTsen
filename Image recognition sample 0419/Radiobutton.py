# -*- coding: utf-8 -*-

import tkinter as tk # 使用Tkinter前需要先導入
# 第1步，產生實體object，建立視窗window
window = tk.Tk()

# 第2步，給窗口的視覺化起名字
window.title('My Window')

# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300') # 這裡的乘是小x

# 第4步，在圖形介面上創建一個標籤label用以顯示並放置
var = tk.StringVar() # 定義一個var用來將radiobutton的值和Label的值聯繫在一起.
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

# 第6步，定義選項觸發函數功能
def print_selection():
	l.config(text='you have selected ' + var.get())

# 第5步，創建三個radiobutton選項，其中variable=var, value='A'的意思就是，當滑鼠選中了其中一個選項，把value的值A放到變數var中，然後賦值給variable
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton

# 第7步，主視窗迴圈顯示
window.mainloop()



