import Tkinter as tk     #tkinter is a gui... in this project, we are using it for easily using the timer with a stop,reset,pause, and quit buttons.

def update_timeText():     
    if (state):
        global timer                                                          
        timer[2] += 1

        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        timeString = pattern.format(timer[0], timer[1], timer[2])
        timeText.configure(text=timeString)
    root.after(10, update_timeText)

def start():
    global state
    state = True

def pause():
    global state
    state = False

def reset():
    global timer
    timer = [0, 0, 0]
    timeText.configure(text='00:00:00')

def exist():
    root.destroy()

state = False

root = tk.Tk()
root.wm_title('Simple Kitchen Timer Example')

timer = [0, 0, 0]
pattern = '{0:02d}:{1:02d}:{2:02d}'

timeText = tk.Label(root, text="00:00:00", font=("Helvetica", 150))
timeText.pack()

startButton = tk.Button(root, text='Start', command=start)
startButton.pack()

pauseButton = tk.Button(root, text='Pause', command=pause)
pauseButton.pack()

resetButton = tk.Button(root, text='Reset', command=reset)
resetButton.pack()

quitButton = tk.Button(root, text='Quit', command=exist)
quitButton.pack()

update_timeText()
root.mainloop()

#We used online sources for certain parts of the code
#That either helped us understand what some of the code
#Was. Although we merged differnt codes from different we
#bsites, we used codes we knew from before. When we got to 
#the tkinter thingy, it was new to us, so we were google-ing
#alot of information about it to understand it better.
# We also tried to interpret a "lap" type of button but
#we couldn't get it to work with the code we had, since the
#code had an under 60 type of method for counting, which counter
#acted with the lapping method
#also just a little disclaimer, even though we have the code add 1
#second until it reaches 60 second where it would then consider it a 
#minute, the code tends to count a bit too slow, so a second isnt really 1 second
