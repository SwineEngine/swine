import math

import swine

if __name__ == "__main__":
    window = swine.Window("Swine Demo", (800, 600), True)
    scene = swine.Scene(window)

    camera = swine.GameObject("Camera")
    camera.add_component(swine.Transform((0, 0, 0), (0, 0, 0, 0), (1, 1, 1)))
    camera.add_component(swine.Camera(window.size, window.size[0] / window.size[1], math.pi / 3, (1024, 0.1)))
    scene.add_object(camera)

    print(scene.get_object("Camera"))

    game_object = swine.GameObject("Pig")

    # game_object.add_component(swine.Transform((0, 0, 0), (0, 0, 0, 0), (1, 1, 1)))

    # FIXME: The library ignores overridden methods
    class TestComponent(swine.Component):
        def update(self):
            print("It just works.")

    # game_object.add_component(TestComponent())

    game_object.add_component(swine.Transform((0, 0, 0), (0, 0, 0, 0), (1, 1, 1)))
    game_object.add_component(swine.RectangleRender((0.15, 0.15)))
    print(game_object.get_components())

    window.add_scene(scene)
    scene.add_object(game_object)

    window.mainloop()
