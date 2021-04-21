# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先導入
 
# 第1步，產生實體object，建立視窗window
window = tk.Tk()
 
# 第2步，給窗口的視覺化起名字
window.title('My Window')
 
# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x
 
# 第4步，在圖形介面上創建一個標籤用以顯示內容並放置
l = tk.Label(window, text='      ', bg='green')
l.pack()
 
# 第10步，定義一個函數功能，用來代表功能表選項的功能，這裡為了操作簡單，定義的功能比較簡單
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter += 1
 
# 第5步，創建一個功能表列，這裡我們可以把他理解成一個容器，在視窗的上方
menubar = tk.Menu(window)
 
# 第6步，創建一個File功能表項目（預設不下拉，下拉內容包括New，Open，Save，Exit功能項）
filemenu = tk.Menu(menubar, tearoff=0)
# 將上面定義的空功能表命名為File，放在功能表列中，就是裝入那個容器中
menubar.add_cascade(label='File', menu=filemenu)
 
# 在File中加入New、Open、Save等小功能表，即我們平時看到的下拉式功能表，每一個小功能表對應命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()    # 添加一條分隔線
filemenu.add_command(label='Exit', command=window.quit) # 用tkinter裡面自帶的quit()函數
 
# 第7步，創建一個Edit功能表項目（預設不下拉，下拉內容包括Cut，Copy，Paste功能項）
editmenu = tk.Menu(menubar, tearoff=0)
# 將上面定義的空功能表命名為 Edit，放在功能表列中，就是裝入那個容器中
menubar.add_cascade(label='Edit', menu=editmenu)
 
# 同樣的在 Edit 中加入Cut、Copy、Paste等小命令功能單元，如果點擊這些單元, 就會觸發do_job的功能
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)
 
# 第8步，創建第二級菜單，即功能表項目裡面的菜單
submenu = tk.Menu(filemenu) # 和上面定義功能表一樣，不過此處實在File上創建一個空的功能表
filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 給放入的菜單submenu命名為Import
 
# 第9步，創建第三級功能表命令，即功能表項目裡面的功能表項目裡面的功能表命令（有點拗口，笑~~~）
submenu.add_command(label='Submenu_1', command=do_job)   # 這裡和上面創建原理也一樣，在Import功能表項目中加入一個小功能表命令Submenu_1
 
# 第11步，創建功能表列完成後，配置讓功能表列menubar顯示出來
window.config(menu=menubar)
 
# 第12步，主視窗迴圈顯示
window.mainloop()


