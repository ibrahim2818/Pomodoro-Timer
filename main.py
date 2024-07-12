from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
 
def countDown(count):
    if count > 0:
        window.after(1000, countDown, count-1)
        print(count)



# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=500, height=400)

countDown(25)





timerLabel= Label(text="Timer", bg=YELLOW, fg="black", font=(FONT_NAME, 35))
timerLabel.grid(column=1, row=0)
file= PhotoImage(file="C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\day 28\\tomato.png")
Canvas= Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
Canvas.create_image(100, 112, image=file)
Canvas.create_text(100, 130, text=f"{25}:00", fill="white", font=(FONT_NAME, 35, "bold"))
Canvas.grid(column=1, row=1)
startButton= Button(text="Start", highlightthickness=0)
startButton.grid(column=0, row=2)
resetButton= Button(text="Reset", highlightthickness=0)
resetButton.grid(column=2, row=2)
CheckLabel= Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16))
CheckLabel.grid(column=1, row=3)


window.mainloop()