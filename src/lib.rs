#[macro_use]
extern crate cpython;
extern crate glutin;

use std::{cell, sync};
use cpython::{Python, PyResult, PyObject};
use glutin::dpi::*;
use glutin::ContextTrait;

py_class!(class Window |py| {
    data running: cell::RefCell<bool>;
    data title: String;
    data vsync: bool;

    def __new__(_cls, title: String, vsync: bool) -> PyResult<Window> {
        Window::create_instance(py, cell::RefCell::new(false), title, vsync)
    }

    def mainloop(&self) -> PyResult<PyObject> {
        self.running(py).replace(true);

        let mut event_loop = glutin::EventsLoop::new();
        // TODO: Make the size a class variable, either a tuple or a vector
        let window_builder = glutin::WindowBuilder::new().with_title(&self.title(py)[..]).with_dimensions(LogicalSize::new(1024.0, 768.0));
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

py_module_initializer!(swine, initswine, PyInit_swine, |py, m| {
    m.add_class::<Window>(py)?;
    Ok(())
});