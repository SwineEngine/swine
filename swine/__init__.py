class Window(object):
    def __init__(self, title, size, vsync):
        self.title = ""
        self.size = ()
        self.vsync = False

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

    def get_object(self, name):
        pass

    def get_object_with_component(self, type_):
        pass


class GameObject(object):
    def __init__(self, name):
        self.name = ""

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


class Camera(Component):
    def __init__(self, size, aspect_ratio, fov, z_plane):
        Component.__init__(self)


class ShapeRender(Component):
    def __init__(self):
        Component.__init__(self)


class RectangleRender(ShapeRender):
    def __init__(self, size):
        ShapeRender.__init__(self)
