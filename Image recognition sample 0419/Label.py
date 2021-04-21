# -*- coding: utf-8 -*-

import tkinter as tk # 使用Tkinter前需要先導入

# 第1步，產生實體object，建立視窗window
window = tk.Tk()

# 第2步，給窗口的視覺化起名字
window.title('My Window')

# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300') # 這裡的乘是小x

# 第4步，在圖形介面上設定標籤
l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# 說明： bg為背景，font為字體，width為長，height為高，這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高

# 第5步，放置標籤
l.pack() # Label內容content區域放置位置，自動調節尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();

# 第6步，主視窗迴圈顯示
window.mainloop()
# 注意，loop因為是迴圈的意思，window.mainloop就會讓window不斷的刷新，如果沒有mainloop,就是一個靜態的window,傳入進去的值就不會有迴圈，
# mainloop就相當於一個很大的while迴圈，有個while，每點擊一次就會更新一次，所以必須要有迴圈 
# 所有的視窗檔都必須有類似的mainloop函數，mainloop是窗口檔的關鍵的關鍵。


