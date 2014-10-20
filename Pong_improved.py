'''
Created on Oct 18, 2014
Mini-project # 4: "Pong: The Game" 
Python MOOC @ Coursera
@author: nirav.chotai

Instructions: Open http://www.codeskulptor.org/
Paste below code, click on play icon and enjoy!
'''

import simplegui
import random

# initialize globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = 0
RIGHT = 1
direction = RIGHT

keymap = simplegui.KEY_MAP
upkey1 = keymap['w']
downkey1 = keymap['s']
upkey2 = keymap['up']
downkey2 = keymap['down']

ball_pos = []
ball_vel = []

paddle_x = [0, WIDTH - PAD_WIDTH - 1]
init_paddle_y = (HEIGHT / 2.0)
paddle_pos = [init_paddle_y, init_paddle_y]
paddle_vel = [0.0, 0.0]
paddle_accel = [1.0, 1.0]
paddle_dir = [0, 0]
accel_inc = 0.5
vel_inc_inc = 0.1
vel_inc = 0.0

score1 = 0
score2 = 0
winner = 0
# score display variables
score_size = HEIGHT / 7
score1x = WIDTH / 3
score1y = HEIGHT / 3
score2x = WIDTH - (WIDTH / 3) - score_size * 2 / 3
score2y = HEIGHT / 3
score_font = 'sans-serif'

main_color = 'White'
ball_color = main_color
ball_wait_color = 'Yellow'

start_point = [WIDTH / 2.0, HEIGHT / 2.0]
endofgame_sleep_len = 1.5 * 60
endofgame_sleep_count = 0
ball_wait_count = 0
ball_wait_inc = BALL_RADIUS / endofgame_sleep_len

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global endofgame_sleep_count
    
    ball_pos = list(start_point)
    endofgame_sleep_count = 0
    velrandx = random.randrange(120, 240) / 60.0
    velrandy = random.randrange(60, 180) / 60.0
    if direction == LEFT:
        velrandx = -velrandx
    #velrandy = -velrandy
    ball_vel = [velrandx, -velrandy]
    
# define event handlers

def new_game():
    # reset some variables for a new game
    global paddle_pos, paddle_vel, paddle_accel, paddle_dir
    global direction, vel_inc, winner

    if winner == 1:
        direction = LEFT
    else:
        direction = RIGHT
    spawn_ball(direction)
    paddle_pos = [init_paddle_y, init_paddle_y]
    paddle_vel = [0.0, 0.0]
    paddle_accel = [1.0, 1.0]
    paddle_dir = [0, 0]
    vel_inc = 0.0

def restart():
    # reset everything, including scores
    global score1, score2, direction, winner
    score1 = score2 = 0
    direction = RIGHT
    winner = 0
    new_game()

# determine if the ball has hit the paddle, returns True / False
def ball_hits_paddle(side):
    ball_y = ball_pos[1]
    paddle_y = paddle_pos[side] + paddle_vel[side]
    return ball_y >= paddle_y - HALF_PAD_HEIGHT and ball_y <= paddle_y + HALF_PAD_HEIGHT

# moves paddle and returns coordinates of corners
# this is probably overly complicated
def get_paddle_pos(N):
    N -= 1
    new = 0
    global paddle_pos, paddle_vel, paddle_accel, paddle_dir
    x = paddle_x[N]
    p = paddle_pos[N]
    d = paddle_dir[N]
    a = paddle_accel[N]
    v = paddle_vel[N]
    
    # going UP
    if d < 0:
        v -= a
        a += accel_inc
    # going DOWN
    elif d > 0:
        v += a
        a += accel_inc
    # key up or no key pressed
    else:
        if a > 1:
            a -= accel_inc
        if a == 0.0:
            new = 1
    
    movement = v
    # hitting top of board
    if p + movement < HALF_PAD_HEIGHT:
        movement = HALF_PAD_HEIGHT - p
        a = 1.0
    # hitting bottom of board
    elif p + movement >= HEIGHT - HALF_PAD_HEIGHT:
        movement = HEIGHT - HALF_PAD_HEIGHT - p - 1
        a = 1.0
    x_left = x
    x_right = x + PAD_WIDTH
    y_upper = p - HALF_PAD_HEIGHT
    y_lower = p + HALF_PAD_HEIGHT
    pll = [x_left,  y_lower + movement]
    plr = [x_right, y_lower + movement]
    pul = [x_left,  y_upper + movement]
    pur = [x_right, y_upper + movement]
    v = movement
    
    # if no motion, then reset paddle to this new position
    if new:
        paddle_pos[N] = v
        paddle_vel[N] = 0
    else:
        paddle_vel[N] = v
        paddle_accel[N] = a

    return [pll, plr, pur, pul]

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, vel_inc
    global endofgame_sleep_count, endofgame_sleep_len, winner
    
    game_over = False
    endofgame_sleep_count += 1
    score1_color = main_color
    score2_color = main_color
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, main_color)
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, main_color)
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, main_color)
    
    # start of game delay and visual effects
    if endofgame_sleep_count < endofgame_sleep_len:
        # draw ball
        line_thick = BALL_RADIUS - ball_wait_inc * endofgame_sleep_count
        ball_rad = BALL_RADIUS - line_thick
        line_buf = line_thick / 2
        canvas.draw_circle(ball_pos, ball_rad + line_buf, line_thick, ball_wait_color, ball_color)
        
    else:
        winner = 0
        # update ball
        ball_pos[0] += ball_vel[0] + (ball_vel[0] * vel_inc)
        ball_pos[1] += ball_vel[1] + (ball_vel[1] * vel_inc)
        
        # draw ball
        canvas.draw_circle(ball_pos, BALL_RADIUS, 1, ball_color, ball_color)
    
        # determine collisions
        if ball_vel[0] < 0:
            # ball travelling left
            xdiff = ball_pos[0] - PAD_WIDTH - BALL_RADIUS
            if xdiff < 0:
                if not ball_hits_paddle(LEFT):
                    score2 += 1
                    winner = 2
                    game_over = True
                vel_inc += vel_inc_inc
                ball_vel[0] = -ball_vel[0]
        else:
            # ball travelling right
            xdiff = WIDTH - 1 - PAD_WIDTH - ball_pos[0] - BALL_RADIUS
            if xdiff < 0:
                if not ball_hits_paddle(RIGHT):
                    score1 += 1
                    winner = 1
                    game_over = True
                vel_inc += vel_inc_inc
                ball_vel[0] = -ball_vel[0]

        if ball_vel[1] < 0:
            # ball travelling up
            ydiff = ball_pos[1] - BALL_RADIUS
            if ydiff < 0:
                ball_vel[1] = -ball_vel[1]
        else:
            # ball travelling down (or horizontal)
            ydiff = HEIGHT - 1 - ball_pos[1] - BALL_RADIUS
            if ydiff < 0:
                ball_vel[1] = -ball_vel[1]
        

    # update paddle's vertical position, keep paddle on the screen
    pos_1 = get_paddle_pos(1)
    pos_2 = get_paddle_pos(2)
    
    # draw paddles
    canvas.draw_polygon(pos_1, 1, main_color, main_color)
    canvas.draw_polygon(pos_2, 1, main_color, main_color)

    # draw scores
    if winner == 1:
        score1_color = ball_wait_color
    elif winner == 2:
        score2_color = ball_wait_color
    canvas.draw_text(str(score1), [score1x, score1y], score_size, score1_color, score_font)
    canvas.draw_text(str(score2), [score2x, score2y], score_size, score2_color, score_font)
    
    if game_over:
        new_game()
        
# a key has been pressed down, see if it's one we care about
def keydown(key):
    # PADDLE 1
    if key == upkey1:
        paddle_dir[0] = -1
    elif key == downkey1:
        paddle_dir[0] = 1
    # PADDLE 2
    elif key == upkey2:
        paddle_dir[1] = -1
    elif key == downkey2:
        paddle_dir[1] = 1
        
# a key has been let up, see if it's one we care about
def keyup(key):
    if key == upkey1:
        paddle_dir[0] = 0
    elif key == downkey1:
        paddle_dir[0] = 0
    elif key == upkey2:
        paddle_dir[1] = 0
    elif key == downkey2:
        paddle_dir[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button('Restart', restart)

# start frame
frame.start()
new_game()

# END