# -*- coding: utf-8 -*-

import tkinter as tk # 使用Tkinter前需要先導入
# 第1步，產生實體object，建立視窗window
window = tk.Tk()

# 第2步，給窗口的視覺化起名字
window.title('My Window')

# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300') # 這裡的乘是小x

# 第4步，在圖形介面上創建一個標籤label用以顯示並放置
var1 = tk.StringVar() # 創建變數，用var1用來接收滑鼠點擊具體選項的內容
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()

# 第6步，創建一個方法用於按鈕的點擊事件
def print_selection():
	value = lb.get(lb.curselection()) # 獲取當前選中的文本
	var1.set(value) # 為label設置值

# 第5步，創建一個按鈕並放置，點擊按鈕調用print_selection函數
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

# 第7步，創建Listbox並為其添加內容
var2 = tk.StringVar()
var2.set((1,2,3,4)) # 為變數var2設置值

# 創建Listbox
lb = tk.Listbox(window, listvariable=var2) #將var2的值賦給Listbox

# 創建一個list並將值迴圈添加到Listbox控制項中
list_items = [11,22,33,44]
for item in list_items:
	lb.insert('end', item) # 從最後一個位置開始加入值

lb.insert(1, 'first') # 在第一個位置加入'first'字元
lb.insert(2, 'second') # 在第二個位置加入'second'字元
lb.delete(2) # 刪除第二個位置的字元
lb.pack()

# 第8步，主視窗迴圈顯示
window.mainloop()


