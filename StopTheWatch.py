'''
Created on Oct 11, 2014
Mini-project # 3: "Stopwatch: The Game" 
Python MOOC @ Coursera
@author: nirav.chotai
'''
# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables
counter = 0
d = 0
x = 0
y = 0
score = "0/0"
pause = True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    a = t / 600
    b = t / 100
    if b>5:
        b=b%6
    d = t % 10        
    c = ((t-d)/10)%10   
    return str(a) + ":" + str(b) + str(c) + "." + str(d) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global pause
    pause = False
    timer.start()
    
def button_stop():
    global d, x, y, score, pause    
    timer.stop()    
    if not pause:
        y=y+1
        if d==0:
            x = x+1   
        score = str(x) + "/" + str(y)
    pause = True
    
def button_reset():
    global counter, d, x, y, score, pause
    counter = 0        
    d = 0
    x = 0
    y = 0
    pause = True
    score = str(x) + "/" + str(y)
    
# define event handler for timer with 0.1 sec interval
def timer_sec(): 
    global counter, pause
    if pause:
        timer.stop()
    counter = counter + 1    
    
# define draw handler
def draw_handler(canvas):    
    canvas.draw_text(format(counter),(80,100),30,"White")    
    canvas.draw_text(score, (160,40), 20, "Green")
    
# create frame
frame = simplegui.create_frame('Stop Watch', 200, 200)
timer = simplegui.create_timer(100, timer_sec)
start = frame.add_button('Start', button_start, 100)
stop = frame.add_button('Stop', button_stop, 100)
reset = frame.add_button('Reset', button_reset, 100)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
