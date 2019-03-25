import swine

if __name__ == "__main__":
    window = swine.Window(title="Swine Demo", vsync=True)
    window.mainloop()
    print(swine, dir(swine), swine.__dict__, sep="\n")
