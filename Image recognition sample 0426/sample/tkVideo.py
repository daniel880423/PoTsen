# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 06:27:13 2021

@author: Alvin
"""

import cv2
import tkinter as tk
from PIL import ImageTk, Image

def video_stream():
    _, pic = cam.read()
    frame = pic.copy()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    videoLabe.imgtk = imgtk
    videoLabe.configure(image=imgtk)
    videoLabe.after(1, video_stream)

root = tk.Tk()
videoFrame = tk.Frame(root, bg="white").pack()
videoLabe = tk.Label(videoFrame)
videoLabe.pack()

cam = cv2.VideoCapture(0)

video_stream()
root.mainloop()