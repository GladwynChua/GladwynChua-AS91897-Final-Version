#Final Version
#libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import Quiz_Interface
from random import shuffle
import sys
import html
import menu


#defining functions 
def quit():
    messagebox.showinfo("General Knowledge Quiz",message="Hope to see you again soon!")
    sys.exit()
   

def name_input():

    global name_entry

    answer2 = name_entry.get()

    if name_entry.get() == "":
        messagebox.showinfo("General Knowledge Quiz",message="Please enter nickname.")
    else:
        messagebox.showinfo("General Knowledge Quiz",message="Hi {}! Get ready to test your general knowledge. ".format(answer2))
        win.destroy()


def age_input():

    global age_entry
    age_input = age_entry.get()

    try:
        if age_entry.get() == "":
            messagebox.showinfo("General Knowledge Quiz",message="Please enter an age.")
    
        elif int(age_input) <= 4:

            messagebox.showinfo("General Knowledge Quiz",message="This must be some sort of joke. Please enter your actual age.")
    
        elif int(age_input) <=12:
            messagebox.showinfo("General Knowledge Quiz",message= "You may need someone to guide you!")
            win_2.destroy() 
        
        elif int(age_input) <=18:

            messagebox.showinfo("General Knowledge Quiz",message="Great age to boost general knowledge!")
            win_2.destroy()
       
        elif int(age_input) <=130:
            messagebox.showinfo("General Knowledge Quiz",message="This quiz should be relatively easy for you!")
            win_2.destroy() 
    
        elif int(age_input) >130:
            messagebox.showinfo(message="This must be some sort of joke. Please enter your actual age.")

    except ValueError:
            messagebox.showinfo(message="Please enter a valid age. (No letters or symbols)")
   

#user details window 1
win=Tk()

win.attributes("-fullscreen",True)

label = Label(win, text="Multiple Choice  Quiz",
                      width=80, height=2, bg="#512E5F", fg="white", font=("Ariel", 50, "bold"))

label.pack(pady= 40)

label_2 = Label(win, text= "Enter Nickname:",width=80, height=2,font=("Ariel", 20))
label_2.pack(pady= 40)
label_2.place(x=-350 , y=310)

quit_button = Button(win, text="Quit", command=quit,
                             width=6,height=2, bg="red", fg="white", font=("ariel", 16, " bold"))

# placing the Quit button on the screen
quit_button.place(x=1240, y=210)


name_entry= Entry(win, width=100)

name_entry.place(relx=0.3, rely=0.55)


name_button =tk.Button(win,text="Enter Nickname",bg="#512E5F", fg="white",width = 20, height = 2,command=name_input)

name_button.place(relx=0.475, rely=0.7)


win.mainloop()


#user details window 2
win_2 = Tk()

win_2.attributes("-fullscreen",True)

label = Label(win_2, text="Multiple Choice  Quiz",
                      width=80, height=2, bg="#512E5F", fg="white", font=("Ariel", 50, "bold"))

label.pack(pady= 40)

label_2 = Label(win_2, text= "Enter Age:",width=80, height=1,font=("Ariel", 20))
label_2.pack(pady= 40)
label_2.place(x=-350 , y=310)

quit_button = Button(win_2, text="Quit", command=quit,
                             width=6,height=2, bg="red", fg="white", font=("ariel", 16, " bold"))

# placing the Quit button on the screen
quit_button.place(x=1240, y=210)

#user enters age
age_entry=Entry(win_2,width=100)

age_entry.place(relx=0.3, rely=0.55)    

#button 
age_button =tk.Button(win_2,text="Enter Age", bg="#512E5F", fg="white",width = 20, height = 2,command=age_input)

age_button.place(relx=0.475, rely=0.7)


win_2.mainloop()

#rules window 3
win_3 = Tk()

win_3.attributes("-fullscreen",True)

label = Label(win_3, text="Multiple Choice  Quiz",
                      width=80, height=2, bg="#512E5F", fg="white", font=("Ariel", 50, "bold"))

label.pack(pady= 40)

next_button = Button(win_3, text="Next", command=win_3.destroy,
                             width=10, bg="green", fg="white", font=("ariel", 20, "bold"))

# places buttons on the screen
next_button.place(x=610, y=650)

# button which quits program entirely
quit_button = Button(win_3, text="Quit", command=quit,
                             width=6,height=2, bg="red", fg="white", font=("ariel", 16, " bold"))

# placing the Quit button on the screen
quit_button.place(x=1240, y=210)

label_2 = Label(win_3, text= "Every answer you get correct you receive one point.",width=80, height=2,font=("Ariel", 20))
label_2.pack(pady= 40)
label_2.place(relx=0.04, rely=0.5)


win_3.mainloop()

#storing questions in question bank
question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)

#variable 
quiz = QuizBrain(question_bank)

#variable
quiz_ui = Quiz_Interface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}") 

menu.link()

#while loop allowing user to restart testing questions
while True:
    answer = askyesno(title='General Knowledge Quiz',
                    message='Do you want to restart the Quiz?')
    if answer:
        quiz = QuizBrain(question_bank)
        quiz_ui = Quiz_Interface(quiz)
    else:
        break
quit()
