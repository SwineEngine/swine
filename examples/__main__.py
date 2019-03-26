import swine

if __name__ == "__main__":
    window = swine.Window("Swine Demo", 800, 600, True)
    scene = swine.Scene(window)

    game_object = swine.GameObject("Pig")

    class TestComponent(swine.Component):
        # FIXME: The library ignores overridden methods
        def update(self, delta_time):
            print("It just works.")

    component = TestComponent()
    game_object.add_component(component)

    window.add_scene(scene)
    scene.add_object(game_object)

    window.mainloop()
