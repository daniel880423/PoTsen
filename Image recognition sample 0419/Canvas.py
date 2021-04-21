# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先導入
 
# 第1步，產生實體object，建立視窗window
window = tk.Tk()
 
# 第2步，給窗口的視覺化起名字
window.title('My Window')
 
# 第3步，設定窗口的大小(長 * 寬)
window.geometry('500x300')  # 這裡的乘是小x
 
# 第4步，在圖形介面上創建 500 * 200 大小的畫布並放置各種元素
canvas = tk.Canvas(window, bg='green', height=200, width=500)
# 說明圖片位置，並導入圖片到畫布上
image_file = tk.PhotoImage(file='image_file.gif')  # 圖片位置（相對路徑，與.py檔同一資料夾下，也可以用絕對路徑，需要給定圖片具體絕對路徑）
image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 圖片錨定點（n圖片頂端的中間點位置）放在畫布（250,0）座標處

# 定義多邊形參數，然後在畫布上畫出指定圖形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 畫直線
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 畫圓 用黃色填充
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 畫扇形 從0度打開收到180度結束
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 畫矩形正方形
canvas.pack()
 
# 第6步，觸發函數，用來一定指定圖形
def moveit():
    canvas.move(rect, 2, 2) # 移動正方形rect（也可以改成其他圖形名字用以移動一起圖形、元素），按每次（x=2, y=2）步長進行移動
 
# 第5步，定義一個按鈕用來移動指定圖形的在畫布上的位置
b = tk.Button(window, text='move item',command=moveit).pack()
 
# 第7步，主視窗迴圈顯示
window.mainloop()


