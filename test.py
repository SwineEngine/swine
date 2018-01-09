import swine
import pyglet

window = swine.Window()
window.title("Test")

scene_one = swine.Scene(window)
scene_two = swine.Scene(window)

label_one = swine.gui.Label(scene_one, text="Hello World!", x=window.width // 2, y=window.height // 2)
label_two = swine.gui.Label(scene_two, text="Bye World!", x=window.width // 2, y=window.height // 2)


class FPS(swine.gui.Label):
    def update(self, event=None):
        self.text = str(round(pyglet.clock.get_fps(), 1))


fps = FPS(scene_one, x=10, y=10)


class AnimatedLabel(swine.gui.Label):
    def start(self, event=None):
        self.frames = ["|+----|", "|-+---|", "|--+--|", "|---+-|", "|----+|",
                       "|---+-|", "|--+--|", "|-+---|"]

        self.current = 0

    def update(self, event=None):
        if self.current < len(self.frames) - 1:
            self.current += 1

        else:
            self.current = 0

        self.text = self.frames[self.current]


anim_label = AnimatedLabel(scene_one, x=window.width // 2, y=window.height // 2 - 30)

image = pyglet.image.load("swine/swine.png")
texture = image.get_texture()
texture.width = 64
texture.height = 64

sprite = swine.Sprite(scene_one, image)


window.mainloop()
