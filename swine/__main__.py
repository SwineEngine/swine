import swine

if __name__ == "__main__":
    window = swine.Window("Swine Demo", (800, 600), True)
    scene = swine.Scene(window)

    game_object = swine.GameObject("Pig")

    window.mainloop()
