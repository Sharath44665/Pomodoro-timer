from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
from turtle import bgpic

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
timer_label=None
check_label=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    my_window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    global timer_label
    timer_label.config(text="timer")
    global  reps
    reps=0
    global check_label
    check_label.config(text="", fg=GREEN, bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        global timer_label
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 22, "bold"))
    elif reps%2==1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 22, "bold"))
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 22, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count>= 0:
        min_count=math.floor(count/60)
        sec_count=count%60
        if sec_count < 10:
            sec_count = f"0{sec_count}"
        global timer
        canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}" )
        timer=my_window.after(250, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        global check_label
        for _ in range(work_sessions):
            mark+="✔"
        check_label = Label(text=f"{mark}", bg=YELLOW)
        check_label.grid(row=3, column=1)

# ---------------------------- UI SETUP ------------------------------- #
my_window=Tk()
my_window.title("PomoDoro")

# def do_something(thing, something, another_thing):
#     print(thing)
#     print(something)
#     print(another_thing)
#
# my_window.after(1000, do_something, "Hello world", "test",456)

my_window.config(padx=100, pady=50, bg=YELLOW)
canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# show tomato image
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)

timer_text=canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,22,"bold"))
# canvas.pack()
canvas.grid(row=1,column=1)

timer_label=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,22,"bold"))
timer_label.grid(row=0,column=1)

start_button=Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button=Button(text="Reset", command=reset_timer)
# reset_button.pack()
reset_button.grid(row=2,column=2)


my_window.mainloop()