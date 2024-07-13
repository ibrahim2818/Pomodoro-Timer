from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps= 0
timer= None
# ---------------------------- TIMER RESET ------------------------------- # 

def resetTimer():
    window.after_cancel(timer)
    timerLabel.config(text="Timer")
    Canvas.itemconfig(timer_text, text=f"{25}:00")
    CheckLabel.config(text="")
    global reps
    reps= 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startCountDown():
    global reps
    reps+= 1
    if reps % 8 == 0:
        countDown(LONG_BREAK_MIN*60 )
        timerLabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countDown(SHORT_BREAK_MIN *60 )
        timerLabel.config(text="Break", fg=PINK)
    else:
        countDown(WORK_MIN *60 )
        timerLabel.config(text="Work", fg=GREEN)
  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
 
def countDown(count):
    count_min= math.floor(count / 60)
    count_sec= count % 60
    if count_sec< 10:
        count_sec= f"0{count_sec}"
        
    Canvas.itemconfig(timer_text,text= f"{count_min}:{count_sec}") 
    if count > 0:
        timer= window.after(1000, countDown, count-1)
    elif count == 0:
        startCountDown()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        CheckLabel.config(text=marks)
    else:
        count_sec= 0
        


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=500, height=400)







timerLabel= Label(text="Timer", bg=YELLOW, fg="black", font=(FONT_NAME, 35))
timerLabel.grid(column=1, row=0)
file= PhotoImage(file="C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\day 28\\tomato.png")
Canvas= Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
Canvas.create_image(100, 112, image=file)
timer_text= Canvas.create_text(100, 130, text=f"{25}:00", fill="white", font=(FONT_NAME, 35, "bold"))
Canvas.grid(column=1, row=1)
startButton= Button(text="Start", highlightthickness=0, command= startCountDown)
startButton.grid(column=0, row=2)
resetButton= Button(text="Reset", highlightthickness=0, command= resetTimer)
resetButton.grid(column=2, row=2)
CheckLabel= Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16))
CheckLabel.grid(column=1, row=3)




window.mainloop()