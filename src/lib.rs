extern crate glutin;
extern crate nalgebra;

use std::{cell, mem, vec};

use pyo3::prelude::*;
use pyo3::types::*;

use glutin::dpi::*;
use glutin::ContextTrait;

use nalgebra::{Vector3, Rotation3};
use nalgebra::geometry::{Translation3, Quaternion};

#[pyclass(gc)]
struct Window {
    title: String,
    size: vec::Vec<f64>,
    vsync: bool,

    running: cell::RefCell<bool>,

    scene_list: cell::RefCell<vec::Vec<PyObject>>,
}

#[pymethods]
impl Window {
    #[new]
    fn __new__(obj: &PyRawObject, title: String, size: &PyTuple, vsync: bool) -> PyResult<()> {
        Ok(obj.init({ Window { title, size: vec!(size.get_item(0).extract()?, size.get_item(1).extract()?), vsync, running: cell::RefCell::new(false), scene_list: cell::RefCell::new(vec::Vec::new()) } }))
    }

    fn add_scene(&self, scene: PyObject) {
        self.scene_list.borrow_mut().push(scene);
    }

    fn mainloop(&self, py: Python) -> PyResult<()> {
        self.running.replace(true);

        let mut event_loop = glutin::EventsLoop::new();
        let window_builder = glutin::WindowBuilder::new().with_title(&self.title[..]).with_dimensions(LogicalSize::new(self.size[0], self.size[1]));
        let windowed_context = glutin::ContextBuilder::new().with_vsync(self.vsync).build_windowed(window_builder, &event_loop).unwrap();

        unsafe {
            windowed_context.make_current().unwrap();

            gl::load_with(|symbol| windowed_context.get_proc_address(symbol) as *const _);
            gl::ClearColor(1.0, 1.0, 1.0, 1.0);
        }

        while self.running.clone().into_inner() {
            event_loop.poll_events(|event| {
                match event {
                    glutin::Event::WindowEvent { event, .. } => match event {
                        glutin::WindowEvent::CloseRequested => {
                            self.close();
                            ()
                        }
                        glutin::WindowEvent::Resized(logical_size) => {
                            let dpi_factor = windowed_context.get_hidpi_factor();
                            windowed_context.resize(logical_size.to_physical(dpi_factor));
                        }
                        _ => ()
                    },
                    _ => ()
                }
            });

            unsafe {
                gl::Clear(gl::COLOR_BUFFER_BIT);
            }

            unsafe {
                for py_scene in self.scene_list.borrow().iter() {
                    // println!("Scene: {:#?}", py_scene);

                    let rust_scene: &Scene = py_scene.extract(py)?;

                    // Loop the objects
                    for py_object in rust_scene.object_list.borrow().iter() {
                        // println!("Object: {:#?}", py_object);

                        let rust_object: &GameObject = py_object.extract(py)?;

                        // Loop the components
                        for py_component in rust_object.component_list.borrow().iter() {
                            // println!("Component: {:#?}", py_component);

                            py_component.call_method1(py, "update", ());

                            let rust_component: &Component = py_component.extract(py)?;

                            // TODO: Calculate the delta time
                            rust_component.update(0f32);
                        }
                    }
                }
            }

            windowed_context.swap_buffers().unwrap();
        }

        Ok(())
    }

    fn close(&self) -> PyResult<()> {
        self.running.replace(false);
        Ok(())
    }
}

#[pyclass(gc, subclass)]
struct Scene {
    window: cell::RefCell<Option<PyObject>>,
    object_list: cell::RefCell<vec::Vec<PyObject>>,
}

#[pymethods]
impl Scene {
    #[new]
    fn __new__(obj: &PyRawObject) -> PyResult<()> {
        Ok(obj.init({ Scene { window: cell::RefCell::new(None), object_list: cell::RefCell::new(vec::Vec::new()) } }))
    }

    fn add_object(&self, object: PyObject) -> PyResult<()> {
        self.object_list.borrow_mut().push(object);
        Ok(())
    }
}

#[pyclass(gc, subclass)]
struct GameObject {
    scene: cell::RefCell<Option<PyObject>>,
    component_list: cell::RefCell<vec::Vec<PyObject>>,
}

#[pymethods]
impl GameObject {
    #[new]
    fn __new__(obj: &PyRawObject) -> PyResult<()> {
        Ok(obj.init({ GameObject { scene: cell::RefCell::new(None), component_list: cell::RefCell::new(vec::Vec::new()) } }))
    }

    fn add_component(&self, component: PyObject) -> PyResult<()> {
        self.component_list.borrow_mut().push(component);
        Ok(())
    }
}

#[pyclass(gc, subclass)]
struct Component {}

#[pymethods]
impl Component {
    #[new]
    fn __new__(obj: &PyRawObject) -> PyResult<()> {
        Ok(obj.init({ Component {} }))
    }

    fn start(&self) -> PyResult<()> {
        Ok(())
    }

    fn update(&self, delta_time: f32) -> PyResult<()> {
        Ok(())
    }

    fn finish(&self) -> PyResult<()> {
        Ok(())
    }
}

#[pyclass(gc, extends = Component)]
struct Transform {
    position: Translation3<f32>,
    rotation: Quaternion<f32>,
    scale: Vector3<f32>,
}

#[pymethods]
impl Transform {
    #[new]
    fn __new__(obj: &PyRawObject, position: &PyTuple, rotation: &PyTuple, scale: &PyTuple) -> PyResult<()> {
        obj.init({
            Transform {
                position: Translation3::new(position.get_item(0).extract()?, position.get_item(1).extract()?, position.get_item(2).extract()?),
                rotation: Quaternion::new(rotation.get_item(0).extract()?, rotation.get_item(1).extract()?, rotation.get_item(2).extract()?, rotation.get_item(3).extract()?),
                scale: Vector3::new(scale.get_item(0).extract()?, scale.get_item(1).extract()?, scale.get_item(2).extract()?),
            }
        });
        Component::__new__(obj);
        Ok(())
    }
}

#[pyclass(gc, extends = Component)]
struct ShapeRender {
}

#[pymethods]
impl ShapeRender {
    #[new]
    fn __new__(obj: &PyRawObject, position: &PyTuple, rotation: &PyTuple, scale: &PyTuple) -> PyResult<()> {
        obj.init({ ShapeRender { } });
        Component::__new__(obj);
        Ok(())
    }
}

#[pyclass(gc, extends = ShapeRender)]
struct SquareRender {
}

#[pymethods]
impl SquareRender {
    #[new]
    fn __new__(obj: &PyRawObject) -> PyResult<()> {
        obj.init({ ShapeRender { } });
        Component::__new__(obj);
        Ok(())
    }

    fn update(&self, delta_time: f32) -> PyResult<()> {
        Ok(())
    }
}

#[pymodule]
fn swine(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Window>()?;
    m.add_class::<Scene>()?;
    m.add_class::<GameObject>()?;
    m.add_class::<Component>()?;
    m.add_class::<Transform>()?;
    m.add_class::<ShapeRender>()?;
    m.add_class::<SquareRender>()?;
    Ok(())
}
