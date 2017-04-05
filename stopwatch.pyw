from tkinter import *

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
state = "IDLE"
def tick():
    global time, state
    if state == "RUNNING":
        display["text"] = str(time)
        display.after(1000, tick)
        time.tick()

def updateTimerState():
    global state, display
    if state == "IDLE":
        state = "RUNNING"
        tick()
    elif state == "RUNNING":
        state = "STOPPED"
    elif state == "STOPPED":
        state = "IDLE"
        time.reset()
        display['text'] = str(time)
        

startPos = [0,0]
def onLeftMouseButtonPress(event):
    global startPos
    startPos[0] = event.x
    startPos[1] = event.y

def onLeftMouseButtonMove(event):
    global root, startPos
    x = root.winfo_x() + event.x - startPos[0]
    y = root.winfo_y() + event.y - startPos[1]
    root.geometry('+%d+%d' % (x,y))

def onLeftMouseButtonRelease(event):
    global startPos
    if event.x == startPos[0] and event.y == startPos[1]:
        updateTimerState()

def onRightMouseButtonRelease(event):
    root.destroy()

root = Tk()
display = Label(root, text=str(time), font=('Consolas', 24))
display.pack()

root.resizable(0,0)
root.attributes("-toolwindow",True)
root.overrideredirect(True)
root.bind("<ButtonRelease-3>", onRightMouseButtonRelease)
root.bind("<ButtonPress-1>", onLeftMouseButtonPress)
root.bind("<B1-Motion>", onLeftMouseButtonMove)
root.bind("<ButtonRelease-1>", onLeftMouseButtonRelease)
root.mainloop()
