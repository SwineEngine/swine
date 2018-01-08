import swine
import pyglet

window = swine.Window()
window.title("Test")

label = swine.gui.Label(window, text="Hello World!", x=window.width // 2, y=window.height // 2)


@window.event
def on_draw():
    window.clear()
    label.draw()


window.mainloop()
