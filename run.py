from Tkinter import *
import datetime

# http://nerdegutta.org/make-a-clock-on-raspberry-pi-with-python-and-35-display.html

''' Function to update time, date'''
def tick():
    now = datetime.datetime.now()

    time_string = now.strftime("%H:%M")
    clock.config(text=time_string)
    clock.after(2000,tick)

    date_string = now.strftime("%a %d %b %y")
    date.config(text=date_string)

''' This function quits the program'''
def quit():
    global window
    window.quit()

''' Make us some workspace'''
window = Tk()
window.overrideredirect(True)
window.geometry("480x320")
window.configure(background='white')

''' Label that shows the time'''
clock = Label(window, font=("serif", 100, "bold"), bg="white")
clock.pack()

''' Label that shows the date'''
date = Label(window, font=("serif", 20, "bold"), bg="white")
date.pack()

''' Quit button in the top left corner'''
quit_btn = Button(window, text="Q", activebackground='red', background='white', command=quit)
quit_btn.place(x=0, y=0)

tick()

window.mainloop()
