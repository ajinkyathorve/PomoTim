#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:40:31 2017

@author: aj
"""


import Tkinter as tk
from PIL import Image, ImageTk


if __name__ == "__main__":
       #Create the main root window
       root = tk.Tk()
       
       #Set the title for the window
       root.title("PomoTim")
       
       #Set the application icon in the taskbar
       icon_img = ImageTk.PhotoImage(file='./images/pticon.ico')
       root.tk.call('wm', 'iconphoto', root._w, icon_img)
       
       #Display welcome and informational text at the top for the user
       top_text = "Welcome to PomoTim, a productivity boosting timer based on the Pomodoro Technique.\n\nYou will be working in sprints of 25 minutes, separated by breaks of 5 minutes.\n\nFour sprints make a set, at the end of which you will get a break of 15 minutes.\n\nLet's get started."
       top_label = tk.Label(root, text=top_text, font=("Arial", 16))
       top_label.grid(row=0,column=0,columnspan=1,sticky=('N','S','E','W'),padx=25,pady=25)
       
       #Display close button to exit the application
       close_button = tk.Button(root, text='CLOSE', width=25, command=root.destroy)
       close_button.grid(row=13,column=0,columnspan=1,pady=25)
       
       #Start the event loop to display everything
       root.mainloop()