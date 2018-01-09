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


window.mainloop()
