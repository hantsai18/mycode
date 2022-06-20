"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This is file that define the object used in breakout clone.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
switch = -1            # Is used to click to start the game


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Define attribute
        self.b_r = ball_radius
        self.p_w = paddle_width
        self.p_h = paddle_height
        self.p_o = paddle_offset

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.rect = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)/2, y=self.window.height-paddle_offset)
        self.rect.filled = True
        self.rect.fill_color = "black"
        self.window.add(self.rect)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window.width-ball_radius*2)/2, y=(self.window.height-ball_radius*2)/2)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__vx = 0
        self.__vy = 0

        # Initialize our mouse listeners
        onmousemoved(self.cursor)
        onmouseclicked(self.start)
        # Draw bricks
        for i in range(10):
            for j in range(10):
                if i < 2:
                    self.brick = GRect(brick_width, brick_height)
                    self.window.add(self.brick, x=0+j*(brick_spacing+brick_width), y=0+i*(brick_spacing+brick_height))
                    self.brick.filled = True
                    self.brick.fill_color = "red"
                elif 1 < i < 4:
                    self.brick = GRect(brick_width, brick_height)
                    self.window.add(self.brick, x=0+j*(brick_spacing+brick_width), y=0+i*(brick_spacing+brick_height))
                    self.brick.filled = True
                    self.brick.fill_color = "orange"
                elif 3 < i < 6:
                    self.brick = GRect(brick_width, brick_height)
                    self.window.add(self.brick, x=0+j*(brick_spacing+brick_width), y=0+i*(brick_spacing+brick_height))
                    self.brick.filled = True
                    self.brick.fill_color = "yellow"
                elif 5 < i < 8:
                    self.brick = GRect(brick_width, brick_height)
                    self.window.add(self.brick, x=0+j*(brick_spacing+brick_width), y=0+i*(brick_spacing+brick_height))
                    self.brick.filled = True
                    self.brick.fill_color = "green"
                else:
                    self.brick = GRect(brick_width, brick_height)
                    self.window.add(self.brick, x=0+j*(brick_spacing+brick_width), y=0+i*(brick_spacing+brick_height))
                    self.brick.filled = True
                    self.brick.fill_color = "blue"

    # Define get and set velocity
    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    def set_vy(self):
        self.__vy *= -1

    def set_vx(self):
        self.__vx *= -1

    # Is used to control paddle
    def cursor(self, mouse):
        if mouse.x < self.p_w/2:
            self.rect.x = 0
        elif mouse.x > self.window.width-self.p_w/2:
            self.rect.x = self.window.width-self.p_w
        else:
            self.rect.x = mouse.x - self.rect.width/2
        self.rect.y = self.window.height-self.p_o-self.p_h

    # Start the game
    def start(self, mouse):
        global switch
        switch = mouse.x
        if self.__vx == 0 and self.__vy == 0:
            if switch > -1:
                self.__vx = random.randint(1, MAX_X_SPEED)
                self.__vy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__vx *= -1

    # Finish the game
    def close(self):
        global switch
        switch = -1
        self.__vx = 0
        self.__vy = 0








