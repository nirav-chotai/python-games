'''
Created on Oct 18, 2014
Mini-project # 4: "Pong: The Game" 
Python MOOC @ Coursera
@author: nirav.chotai

Instructions: Open http://www.codeskulptor.org/
Paste below code, click on play icon and enjoy!
'''

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = [0, 160] 
paddle2_pos = [0, 160] 
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, sign 
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    
    #randomly select velocity
    if direction == RIGHT:
        sign = 1
    elif direction == LEFT:
        sign = -1
    hor_vel = random.randrange(2, 5)
    ver_vel = random.randrange(1, 4)
    ball_vel[0] = sign * hor_vel
    ball_vel[1] = -ver_vel
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel 
    global score1, score2, sign   
    score1 = 0
    score2 = 0
    #randomly select RIGHT or LEFT
    TF = random.choice([0, 1])
    if TF == 0:
        direction = RIGHT
    elif TF == 1:
        direction = LEFT
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos 
    global ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #print ball_pos[0]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # Collision with left gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
    # Collision with right gutter
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH - 1:
        if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT:
                ball_vel[0] = -ball_vel[0]*1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
    # Collision with top wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # Collision with bottom wall
    if ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
        ball_vel[1] = -ball_vel[1]
    
    # draw paddles
    canvas.draw_line((0, paddle1_pos[1]), (0, paddle1_pos[1] + PAD_HEIGHT), 16, "White")
    canvas.draw_line((WIDTH, paddle2_pos[1]), (WIDTH, paddle2_pos[1] + PAD_HEIGHT), 16, "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    if paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle1_vel[1] = 0
    if paddle2_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle2_vel[1] = 0
    if paddle1_pos[1] <= 0:
        paddle1_vel[1] = 0
    if paddle2_pos[1] <= 0:
        paddle2_vel[1] = 0
    
    # draw scores
    canvas.draw_text(str(score1), (140, 80), 50, "White")
    canvas.draw_text(str(score2), (440, 80), 50, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key == simplegui.KEY_MAP["S"]:
        if paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] +=acc
    if key == simplegui.KEY_MAP["down"]:
        if paddle2_pos[1] >= HEIGHT - PAD_HEIGHT:
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] +=acc
    if key == simplegui.KEY_MAP["W"]:
        if paddle1_pos[1] <= 0:
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] -=acc
    if key == simplegui.KEY_MAP["up"]:
        if paddle2_pos[1] <= 0:
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] -=acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["S"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    if key == simplegui.KEY_MAP["W"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 150)


# start frame
new_game()
frame.start()
