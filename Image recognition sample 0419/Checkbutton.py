# -*- coding: utf-8 -*-

import tkinter as tk # 使用Tkinter前需要先導入
# 第1步，產生實體object，建立視窗window
window = tk.Tk()

# 第2步，給窗口的視覺化起名字
window.title('My Window')

# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300') # 這裡的乘是小x

# 第4步，在圖形介面上創建一個標籤label用以顯示並放置
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

# 第6步，定義觸發函數功能
def print_selection():
	if (var1.get() == 1) & (var2.get() == 0): # 如果選中第一個選項，未選中第二個選項
		l.config(text='I love only Python ')
	elif (var1.get() == 0) & (var2.get() == 1): # 如果選中第二個選項，未選中第一個選項
		l.config(text='I love only C++')
	elif (var1.get() == 0) & (var2.get() == 0): # 如果兩個選項都未選中
		l.config(text='I do not love either')
	else:
		l.config(text='I love both') # 如果兩個選項都選中

# 第5步，定義兩個Checkbutton選項並放置
var1 = tk.IntVar() # 定義var1和var2整型變數用來存放選擇行為返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection) # 傳值原理類似於radiobutton部件
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

# 第7步，主視窗迴圈顯示
window.mainloop()

