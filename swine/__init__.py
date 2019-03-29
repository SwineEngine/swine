class Window(object):
    def __init__(self, title, size, vsync):
        pass

    def add_scene(self, scene):
        pass

    def mainloop(self):
        pass

    def close(self):
        pass


class Scene(object):
    def __init__(self, window):
        self.window = Window

    def add_object(self, game_object):
        pass


class GameObject(object):
    def __init__(self, name):
        self.name = str

    def add_component(self, component):
        pass


class Component(object):
    def __init__(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def finish(self):
        pass


class Transform(Component):
    def __init__(self, position, rotation, scale):
        Component.__init__(self)


class ShapeRender(Component):
    def __init__(self):
        Component.__init__(self)


class RectangleRender(Component):
    def __init__(self, size):
        Component.__init__(self)
