import swine

if __name__ == "__main__":
    window = swine.Window("Swine Demo", (800, 600), True)
    scene = swine.Scene(window)

    game_object = swine.GameObject("Pig")

    # FIXME: The library ignores overridden methods
    # class TestComponent(swine.Component):
    #     def update(self, delta_time):
    #         print("It just works.")

    # component = TestComponent()
    # game_object.add_component(component)

    game_object.add_component(swine.Transform((0, 0, 0), (0, 0, 0, 0), (1, 1, 1)))

    window.add_scene(scene)
    scene.add_object(game_object)

    window.mainloop()