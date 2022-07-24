
#Import the required libraries
from tkinter import *
import tkinter as tk
from tkinter import Label 
import sys
from tkinter import messagebox

def credits_message():
   messagebox.showinfo("General Knowledge Quiz",message="This code was developed by Gladwyn Chua ©")

def link():
   print("Loading.....")
   print("Directing to Main Menu")

def quit():
   messagebox.showinfo("General Knowledge Quiz",message="Hope to see you again soon!")
   sys.exit()

def menu_popup(event):
   # display the popup menu
   try:
      popup.tk_popup(event.x_root, event.y_root, 0)
   finally:
      #Release the grab
      popup.grab_release()  

   
#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of the Tkinter library
win.attributes("-fullscreen", True)

label = Label(win, text="Multiple Choice  Quiz",
                      width=80, height=2, bg="#512E5F", fg="white", font=("Ariel", 50, "bold"))

label.pack(pady= 40)

#Add Menu
popup = Menu(win, tearoff=0) 

start = tk.Button(win, text="Start", bg="#512E5F", command=win.destroy, width = 20,  fg="white", font=('Ariel', 45,))
start.place(relx=0.25, rely=0.32)

recognition = tk.Button(win, text="Credit", bg="#512E5F", command=credits_message, width = 20,  fg="white", font=('Ariel', 45,))
recognition.place(relx=0.25, rely=0.52)


exit = tk.Button(win, text="Quit", bg="#512E5F", command=quit, width = 20, fg="white",font=('Ariel', 45))
exit.place(relx=0.25, rely=0.72)

mainloop()





