"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is the breakout clone.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10     # 100 frames per second
NUM_LIVES = 10		# Number of attempts
num_brick = 0       # Number of brick that is removed
graphics = BreakoutGraphics()


def main():
    global num_brick
    for i in range(NUM_LIVES):
        while True:
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            graphics.ball.move(vx, vy)
            check_object()
            check_wall()
            # When ball fall over the window or remove all bricks
            if graphics.ball.y + graphics.ball.height > graphics.window.height or num_brick == 100:
                graphics.ball.x = (graphics.window.width - graphics.b_r * 2) / 2
                graphics.ball.y = (graphics.window.height - graphics.b_r * 2) / 2
                graphics.close()
                break
            pause(FRAME_RATE)


def check_object():
    """
    This is function that check if ball contact with brick or paddle.
    """
    global num_brick
    obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
    obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.b_r * 2, graphics.ball.y)
    obj3 = graphics.window.get_object_at(graphics.ball.x + graphics.b_r * 2, graphics.ball.y + graphics.b_r * 2)
    obj4 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.b_r * 2)
    if obj1 is not None:
        if obj1 is not graphics.rect:
            graphics.window.remove(obj1)
            num_brick += 1
            graphics.set_vy()
        else:
            graphics.ball.y = obj1.y - graphics.b_r*2
            graphics.set_vy()
    elif obj2 is not None:
        if obj2 is not graphics.rect:
            graphics.window.remove(obj2)
            num_brick += 1
            graphics.set_vy()
        else:
            graphics.ball.y = obj2.y - graphics.b_r*2
            graphics.set_vy()
    elif obj3 is not None:
        if obj3 is not graphics.rect:
            graphics.window.remove(obj3)
            num_brick += 1
            graphics.set_vy()
        else:
            graphics.ball.y = obj3.y - graphics.b_r*2
            graphics.set_vy()
    elif obj4 is not None:
        if obj4 is not graphics.rect:
            graphics.window.remove(obj4)
            num_brick += 1
            graphics.set_vy()
        else:
            graphics.ball.y = obj4.y - graphics.b_r*2
            graphics.set_vy()


def check_wall():
    """
    This is function that check if ball contact with wall.
    """
    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
        graphics.set_vx()
    if graphics.ball.y <= 0:
        graphics.set_vy()


if __name__ == '__main__':
    main()
