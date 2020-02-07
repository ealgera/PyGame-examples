import pyglet
from pyglet.gl import *
from random import randint
from math import sin, cos, pi
from pyglet import window, clock, font, text
from pyglet.window import key

WIDTH  = 800
HEIGHT = 600
AANTAL_CIRKELS = 100

class RandomCirkel():

    def __init__(self):
        self.r = randint(20, 25)
        self.x = int(WIDTH / 2) + randint(-50, 50)
        self.y = int(HEIGHT / 2)  + randint(-50, 50)
        self.xspeed = randint(-20, 20)
        self.yspeed = randint(-10, 10)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        print(f"Cirkel: x={self.x}, y={self.y}, r={self.r}")

    def show(self):
        iterations = int(2*self.r*pi)
        s = sin(2*pi / iterations)
        c = cos(2*pi / iterations)

        dx, dy = self.r, 0

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y)
        for i in range(iterations+1):
            glColor3ub(self.color[0],self.color[1],self.color[2])
            glVertex2f(self.x+dx, self.y+dy)
            dx, dy = (dx*c - dy*s), (dy*c + dx*s)
        glEnd()

    def move(self):
        self.x += self.xspeed
        if (self.x - self.r) < 0 or (self.x + self.r) > WIDTH:
            self.xspeed = self.xspeed * -1

        self.y += self.yspeed
        if (self.y - self.r) < 0 or (self.y + self.r) > HEIGHT:
            self.yspeed = self.yspeed * -1

class MyWindows(window.Window):

    def __init__(self, *args, **kwargs):
        self.win = window.Window.__init__(self, *args, **kwargs)
        self.cirkels = [RandomCirkel() for x in range(AANTAL_CIRKELS)]

        clock.schedule_interval(self.update, 1.0/30)

    def update(self, dt):
        pass

    def on_draw(self):
        self.clear()
        clock.tick()

        for cirkel in self.cirkels:
            cirkel.show()
            cirkel.move()

        self.label = text.Label(text=f"FPS: {int(clock.get_fps())}", font_name="Tahoma", font_size=20, y=10)
        self.label.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.dispatch_("on_close")

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

if __name__ == "__main__":
    win = MyWindows(caption="Een Window", width=WIDTH, height=HEIGHT)

    pyglet.app.run()
