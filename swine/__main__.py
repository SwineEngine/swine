import swine

if __name__ == "__main__":
    window = swine.Window("Swine Demo", (800, 600), True)

    scene = swine.Scene(window)
    window.add_scene(scene)

    game_object = swine.GameObject("Pig")
    scene.add_object(game_object)

    component = swine.Component()
    game_object.add_component(component)

    window.mainloop()
