from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
from turtle import bgpic

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
def click_on_start():
    count_down(5)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count>= 0:
        canvas.itemconfig(timer_text, text=count)
        my_window.after(1000, count_down, count-1)
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

start_button=Button(text="Start", command=click_on_start)
start_button.grid(row=2, column=0)

reset_button=Button(text="Reset")
# reset_button.pack()
reset_button.grid(row=2,column=2)

check_label=Label(text="✔", fg=GREEN, bg=YELLOW)
check_label.grid(row=3,column=1)
my_window.mainloop()