from tkinter import *

root = Tk()

state = "IDLE"

class Time:
    def __init__(self):
        self.reset()

    def reset(self):
        self.hours = 0
        self.mins = 0
        self.secs = 0

    def tick(self):
        self.secs += 1
        if self.secs == 60:
            self.secs = 0
            self.mins += 1
        if self.mins == 60:
            self.mins = 0
            self.hours += 1

    def __str__(self):
        return "{}:{:02}:{:02}".format(time.hours,
                                       time.mins,
                                       time.secs)

time = Time()

def tick():
    global time, state
    if state == "RUNNING":
        display["text"] = str(time)
        display.after(1000, tick)
        time.tick()

def handler():
    global state, display, button
    if state == "IDLE":
        state = "RUNNING"
        button['text'] = "stop"
        tick()
    elif state == "RUNNING":
        state = "STOPPED"
        button['text'] = "stopped"
    elif state == "STOPPED":
        state = "IDLE"
        time.reset()
        display['text'] = str(time)
        button['text'] = "start"
        

display = Label(root, text=str(time), font=('Consolas', 24))
display.pack()

button = Button(root, text="start", command=handler)
button.pack()

root.resizable(0,0)

root.mainloop()
