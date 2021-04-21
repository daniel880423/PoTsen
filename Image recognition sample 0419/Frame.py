# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先導入
 
# 第1步，產生實體object，建立視窗window
window = tk.Tk()
 
# 第2步，給窗口的視覺化起名字
window.title('My Window')
 
# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x
 
# 第4步，在圖形介面上創建一個標籤用以顯示內容並放置
tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()   # 和前面部件分開創建和放置不同，其實可以創建和放置一步完成
 
# 第5步，創建一個主frame，長在主window窗口上
frame = tk.Frame(window)
frame.pack()
 
# 第6步，創建第二層框架frame，長在主框架frame上面
frame_l = tk.Frame(frame)# 第二層frame，左frame，長在主frame上
frame_r = tk.Frame(frame)# 第二層frame，右frame，長在主frame上
frame_l.pack(side='left')
frame_r.pack(side='right')
 
# 第7步，創建三組標籤，為第二層frame上面的內容，分為左區域和右區域，用不同顏色標識
tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()
 
# 第8步，主視窗迴圈顯示
window.mainloop()

