import swine
import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = swine.Window()
window.title("Test")

scene_one = swine.Scene(window)
scene_two = swine.Scene(window)

label_one = swine.gui.Label(scene_one, text="Hello World!", x=window.width // 2, y=window.height // 2, layer=2)
label_two = swine.gui.Label(scene_two, text="Bye World!", x=window.width // 2, y=window.height // 2)


class FPSLabel(swine.gui.Label):
    def update(self, dt=None):
        self.text = str(round(pyglet.clock.get_fps(), 1))


fps = FPSLabel(scene_one, x=10, y=10)


class AnimatedLabel(swine.gui.Label):
    def __init__(self, scene, x, y):
        swine.gui.Label.__init__(self, scene, text="", x=x, y=y, layer=0)
        self.frames = ["[+---------]", "[-+--------]", "[--+-------]", "[---+------]", "[----+-----]", "[-----+----]", "[------+---]", "[-------+--]", "[--------+-]", "[---------+]"]

        self.current = 0

    def update(self, dt=None):
        if self.current < len(self.frames) - 1:
            self.current += 1

        else:
            self.current = 0

        self.text = self.frames[self.current]


anim_label = AnimatedLabel(scene_one, x=window.width // 2, y=window.height // 2 - 30)


class Pig(swine.Sprite):
    image = pyglet.image.load("swine/swine.png")
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

    def __init__(self):
        swine.Sprite.__init__(self, scene_one, Pig.image, 6, layer=1)
        self.x = self.window.width // 2
        self.y = self.window.height // 2

        self.scale_x = 1

    def update(self, dt=None):
        speed = dt * swine.FPS

        if self.keys[key.LSHIFT]:
            speed *= 2

        if self.keys[key.W]:
            # print("W")
            self.y += speed

        if self.keys[key.A]:
            # print("A")
            self.x -= speed
            self.scale_x = -1

        if self.keys[key.S]:
            # print("S")
            self.y -= speed

        if self.keys[key.D]:
            # print("D")
            self.x += speed
            self.scale_x = 1

    def on_key_press(self, symbol, modifiers):
        print(key.symbol_string(symbol))

    def on_mouse_press(self, x, y, button, modifiers):
        print(mouse.buttons_string(button))


pig = Pig()

line = swine.Line(scene_one, 100, 5, 100, 50, 0, [swine.RED])
rect = swine.Rectangle(scene_one, 100, 50, True, 50, 50, 0, swine.GREEN)
squ = swine.Square(scene_one, 50, True, 25, 20, 0, [swine.BLUE, swine.RED])

window.mainloop()
