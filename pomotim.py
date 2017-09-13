#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:40:31 2017

@author: aj
"""


import Tkinter as tk
from PIL import Image, ImageTk


def countdown(time, time_list):
       return


def more_info():
       return


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
       top_label.grid(row=0,column=0,columnspan=2,sticky=('N','S','E','W'),padx=25,pady=25)
       
       #Display start button to start the countdown
       start_button = tk.Button(root, text='START', width=25, command=lambda:countdown(5, time_list))
       start_button.grid(row=1,column=0,sticky=('E'),padx=40,pady=25)
       
       #Display more info button, opens Wiki page about Pomodoro Technique
       info_button = tk.Button(root, text='MORE INFO', width=25, command=more_info)
       info_button.grid(row=1,column=1,sticky=('W'),padx=40,pady=25)
       
       #Countdown timer in MM:SS format
       time_label = tk.Label(text="25:00", font=("Arial", 48))
       time_label.grid(row=2,column=0,columnspan=2,pady=25)
       
       #List of tasks, labelled Sprint 1, Break 1 through Sprint 4, Break 4
       status_names = ["Sprint 1", "Break 1", "Sprint 2", "Break 2", "Sprint 3", "Break 3", "Sprint 4", "Break 4"]
       row_num = 3
       for name in status_names:
              state = tk.Label(text=name+": ", font=("Arial", 12)).grid(row=row_num,column=0,sticky=('E'),padx=20,pady=5)
              progress = tk.Label(text="", font=("Arial", 12)).grid(row=row_num,column=1,sticky=('E'),padx=20,pady=5)
              row_num += 1
       
       #Display close button to exit the application
       close_button = tk.Button(root, text='CLOSE', width=25, command=root.destroy)
       close_button.grid(row=13,column=0,columnspan=2,pady=25)
       
       #List with time in seconds for the various tasks, ordered reverse from Break 4, Sprint 4 through Break 1
       time_list = [900,1500,300,1500,300,1500,30]
       
       #Configuring rows and columns to handle how resizing affects them
       for i in range(0,2):
              root.columnconfigure(i, weight=1)
       for i in range(0,14):
              root.rowconfigure(i, weight=1)
       
       #Start the event loop to display everything
       root.mainloop()