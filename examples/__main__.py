import swine

if __name__ == "__main__":
    window = swine.Window("Swine Demo", (800, 600), True)
    scene = swine.Scene(window)

    game_object = swine.GameObject("Pig")

    # game_object.add_component(swine.Transform((0, 0, 0), (0, 0, 0, 0), (1, 1, 1)))

    # FIXME: The library ignores overridden methods
    class TestComponent(swine.Component):
        def update(self):
            print("It just works.")

    # game_object.add_component(TestComponent())

    # game_object.add_component(swine.Transform((0, 0, 0), (0, 0, 0, 0), (1, 1, 1)))
    game_object.add_component(swine.RectangleRender((0.15, 0.15)))

    window.add_scene(scene)
    scene.add_object(game_object)

    window.mainloop()
