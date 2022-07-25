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

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 138, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

label_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, 'bold'))
label_title.grid(row=0, column=1)

but_start = Button(text="Start", font=(FONT_NAME, 15, 'bold'))
but_start.grid(row=2, column=0)

but_reset = Button(text="Reset", font=(FONT_NAME, 15, 'bold'))
but_reset.grid(row=2, column=2)

window.mainloop()


