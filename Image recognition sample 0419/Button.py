# -*- coding: utf-8 -*-

import tkinter as tk # 使用Tkinter前需要先導入
# 第1步，產生實體object，建立視窗window
window = tk.Tk()

# 第2步，給窗口的視覺化起名字
window.title('My Window')

# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300') # 這裡的乘是小x

# 第4步，在圖形介面上設定標籤
var = tk.StringVar() # 將label標籤的內容設置為字元類型，用var來接收hit_me函數的傳出內容用以顯示在標籤上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 說明： bg為背景，fg為字體顏色，font為字體，width為長，height為高，這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高
l.pack()

# 定義一個函數功能(內容自己自由編寫)，供點擊Button按鍵時呼叫，呼叫命令參數command=函數名
on_hit = False
def hit_me():
	global on_hit
	if on_hit == False:
		on_hit = True
		var.set('you hit me')
	else:
		on_hit = False
		var.set('')
# 第5步，在視窗介面設置放置Button按鍵

b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()

# 第6步，主視窗迴圈顯示
window.mainloop()


