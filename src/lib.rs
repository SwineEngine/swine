#[macro_use]
extern crate cpython;
extern crate glutin;

use std::{cell, mem, vec};
use cpython::*;
use glutin::dpi::*;
use glutin::ContextTrait;

py_class!(class Window |py| {
    data running: cell::RefCell<bool>;
    data title: String;
    data size: PyTuple;
    data vsync: bool;

    def __new__(_cls, title: String, size: PyTuple, vsync: bool) -> PyResult<Window> {
        Window::create_instance(py, cell::RefCell::new(false), title, size, vsync)
    }

    def mainloop(&self) -> PyResult<PyObject> {
        self.running(py).replace(true);

        let size_x: f64;
        let size_y: f64;

        unsafe {
            // This can probably be done better
            size_x = (*self.size(py)).get_item(py, 0).unchecked_cast_into::<PyFloat>().value(py);
            size_y = (*self.size(py)).get_item(py, 1).unchecked_cast_into::<PyFloat>().value(py);
        }

        let mut event_loop = glutin::EventsLoop::new();
        let window_builder = glutin::WindowBuilder::new().with_title(&self.title(py)[..]).with_dimensions(LogicalSize::new(size_x, size_y));
        let windowed_context = glutin::ContextBuilder::new().with_vsync(*self.vsync(py)).build_windowed(window_builder, &event_loop).unwrap();

        unsafe {
            windowed_context.make_current().unwrap();

            gl::load_with(|symbol| windowed_context.get_proc_address(symbol) as *const _);
            gl::ClearColor(1.0, 1.0, 1.0, 1.0);
        }

        while self.running(py).clone().into_inner() {
            event_loop.poll_events(|event| {
                match event {
                    glutin::Event::WindowEvent{ event, .. } => match event {
                        glutin::WindowEvent::CloseRequested => {
                            self.running(py).replace(false);
                            ()
                        },
                        glutin::WindowEvent::Resized(logical_size) => {
                            let dpi_factor = windowed_context.get_hidpi_factor();
                            windowed_context.resize(logical_size.to_physical(dpi_factor));
                        },
                        _ => ()
                    },
                    _ => ()
                }
            });

            unsafe {
                gl::Clear(gl::COLOR_BUFFER_BIT);
            }

            windowed_context.swap_buffers().unwrap();
        }

        Ok(py.None())
    }

    def close(&self) -> PyResult<PyObject> {
        self.running(py).replace(false);
        Ok(py.None())
    }
});

py_class!(class Scene |py| {
    data window: cell::RefCell<Option<PyObject>>;
    data object_list: *mut vec::Vec<PyObject>;

    def __new__(_cls, window: PyObject, object_list: &mut vec::Vec<PyObject>) -> PyResult<Scene> {
        Scene::create_instance(py, cell::RefCell::new(Some(window)), object_list)
    }

    def __traverse__(&self, visit) {
        if let Some(ref obj) = *self.window(py).borrow() {
            visit.call(obj);
        }
        Ok(())
    }

    def __clear__(&self) {
        let old_window = mem::replace(&mut *self.window(py).borrow_mut(), None);
        old_window.release_ref(py);
    }

    def add_object(&self, object: PyObject) -> PyResult<PyObject> {
        // TODO: Push to the object_list

        Ok(py.None())
    }
});

py_class!(class GameObject |py| {
    data scene: cell::RefCell<Option<PyObject>>;
    data name: String;
    data component_list: *mut vec::Vec<PyObject>;

    def __new__(_cls, name: String) -> PyResult<GameObject> {
        GameObject::create_instance(py, cell::RefCell::new(None), name, &mut vec::Vec::new())
    }

    def __traverse__(&self, visit) {
        if let Some(ref obj) = *self.scene(py).borrow() {
            visit.call(obj);
        }
        Ok(())
    }

    def __clear__(&self) {
        let old_scene = mem::replace(&mut *self.scene(py).borrow_mut(), None);
        old_scene.release_ref(py);
    }

    def add_component(&self, component: PyObject) -> PyResult<PyObject> {
        // TODO: Push to the component_list

        Ok(py.None())
    }
});

py_class!(class Component |py| {
    def __new__(_cls) -> PyResult<Component> {
        Component::create_instance(py)
    }

    def start(&self) -> PyResult<PyObject> {
        Ok(py.None())
    }

    def update(&self, delta_time) -> PyResult<PyObject> {
        Ok(py.None())
    }

    def finish(&self) -> PyResult<PyObject> {
        Ok(py.None())
    }
});

py_module_initializer!(swine, initswine, PyInit_swine, |py, m| {
    m.add_class::<Window>(py)?;
    m.add_class::<Scene>(py)?;
    m.add_class::<GameObject>(py)?;
    m.add_class::<Component>(py)?;
    Ok(())
});