# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先導入
 
# 第1步，產生實體object，建立視窗window
window = tk.Tk()
 
# 第2步，給窗口的視覺化起名字
window.title('My Window')
 
# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x
 
# 第4步，pack 放置方法
tk.Label(window, text='P', fg='red').pack(side='top')    # 上
tk.Label(window, text='P', fg='red').pack(side='bottom') # 下
tk.Label(window, text='P', fg='red').pack(side='left')   # 左
tk.Label(window, text='P', fg='red').pack(side='right')  # 右
 
# 第5步，主視窗迴圈顯示
window.mainloop()
