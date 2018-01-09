import swine
import pyglet
from pyglet.window import key

window = swine.Window()
window.title("Test")

scene_one = swine.Scene(window)
scene_two = swine.Scene(window)

label_one = swine.gui.Label(scene_one, text="Hello World!", x=window.width // 2, y=window.height // 2, layer=2)
label_two = swine.gui.Label(scene_two, text="Bye World!", x=window.width // 2, y=window.height // 2)


class FPS(swine.gui.Label):
    def update(self, event=None):
        self.text = str(round(pyglet.clock.get_fps(), 1))


fps = FPS(scene_one, x=10, y=10)


class AnimatedLabel(swine.gui.Label):
    def __init__(self, scene, x, y):
        swine.gui.Label.__init__(self, scene, text="", x=x, y=y, layer=0)
        self.frames = ["[+---------]", "[-+--------]", "[--+-------]", "[---+------]", "[----+-----]", "[-----+----]", "[------+---]", "[-------+--]", "[--------+-]", "[---------+]"]

        self.current = 0

    def update(self, event=None):
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
        self.speed = 3

    def update(self, event=None):
        if self.keys[key.W]:
            # print("W")
            self.y += self.speed

        if self.keys[key.A]:
            # print("A")
            self.x -= self.speed
            self.scale_x = -1

        if self.keys[key.S]:
            # print("S")
            self.y -= self.speed

        if self.keys[key.D]:
            # print("D")
            self.x += self.speed
            self.scale_x = 1


pig = Pig()


window.mainloop()
