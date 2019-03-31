// extern crate glutin;
#[macro_use]
extern crate glium;
extern crate nalgebra;
// extern crate gl;

use std::{cell, vec, fs, io, string};
use std::borrow::Borrow;
use std::io::prelude::*;
use std::f64::consts::PI;

use pyo3::prelude::*;
use pyo3::types::*;

use glium::{glutin, Surface};

use nalgebra::{Vector2, Vector3};
use nalgebra::geometry::{Translation3, Quaternion};

#[derive(Copy, Clone)]
struct Vertex {
    position: [f32; 2],
}
implement_vertex!(Vertex, position);

impl ToPyObject for Vertex {
    fn to_object(&self, py: Python) -> PyObject {
        PyTuple::new(py, &[self.position[0], self.position[1]]).to_object(py)
    }
}

#[pyclass(gc)]
struct Window {
    #[pyo3(get)]
    title: String,
    #[pyo3(get)]
    size: vec::Vec<f64>,
    #[pyo3(get)]
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
        let window_builder = glutin::WindowBuilder::new().with_title(&self.title[..]).with_dimensions(glutin::dpi::LogicalSize::new(self.size[0], self.size[1]));
        let windowed_context = glutin::ContextBuilder::new(); // .with_vsync(self.vsync).build_windowed(window_builder, &event_loop).unwrap();

        let display = glium::Display::new(window_builder, windowed_context, &event_loop).unwrap();

        unsafe {
            // windowed_context.make_current().unwrap();

            // gl::load_with(|symbol| windowed_context.get_proc_address(symbol) as *const _);
            // gl::ClearColor(1.0, 1.0, 1.0, 1.0);
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
                            // let dpi_factor = windowed_context.get_hidpi_factor();
                            // windowed_context.resize(logical_size.to_physical(dpi_factor));
                        }
                        _ => ()
                    },
                    _ => ()
                }
            });

            unsafe {
                // gl::Clear(gl::COLOR_BUFFER_BIT);
            }

            let mut target = display.draw();
            target.clear_color(0.0, 0.0, 0.0, 1.0);

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

                            // TODO: Calculate the delta time
                            py_component.call_method1(py, "update", ())?;

                            let draw_structs = py_component.call_method1(py, "draw", ())?;
                            // println!("{:#?}", draw_structs);

                            let draw_structs_list: &PyList = match draw_structs.cast_as::<PyList>(py) {
                                Ok(draw_structs_list) => draw_structs_list,
                                Err(error) => continue
                            };

                            let mut vector: vec::Vec<Vertex> = vec::Vec::new();
                            let mut name: String = String::from("");

                            let mut index = 0;
                            for list_item in draw_structs_list.iter() {
                                // println!("{}", list_item);

                                if index == 0 {
                                    // FIXME: Could probably check if the struct was None rather than expecting an error
                                    let rust_item: &PyList = match list_item.try_into() {
                                        Ok(rust_item) => rust_item,
                                        Err(error) => continue
                                    };

                                    for vertex in rust_item.iter() {
                                        let vertex_tuple: &PyTuple = vertex.try_into()?;
                                        let rust_vertex = Vertex {
                                            position: [vertex_tuple.get_item(0).extract()?,
                                                vertex_tuple.get_item(1).extract()?]
                                        };

                                        // println!("{:#?}", vertex_tuple);
                                        vector.push(rust_vertex)
                                    }
                                }

                                if index == 1 {
                                    let py_string: &PyString = list_item.try_into()?;

                                    name = py_string.to_string()?.to_string();
                                }

                                index += 1;
                            }

                            let vertex_buffer = glium::VertexBuffer::new(&display, &vector).unwrap();
                            let indices = glium::index::NoIndices(glium::index::PrimitiveType::TriangleFan);

                            // TODO: Gather all the shaders when the game begins and store them somewhere
                            let vertex_file = fs::File::open(format!("../resources/shaders/{}.vert", name))?;
                            let mut vertex_contents = String::new();

                            let mut buf_reader = io::BufReader::new(vertex_file);
                            buf_reader.read_to_string(&mut vertex_contents)?;

                            let fragment_file = fs::File::open(format!("../resources/shaders/{}.frag", name))?;
                            let mut fragment_contents = String::new();

                            buf_reader = io::BufReader::new(fragment_file);
                            buf_reader.read_to_string(&mut fragment_contents)?;

                            let program = glium::Program::from_source(&display, &vertex_contents, &fragment_contents, None).unwrap();

                            target.draw(&vertex_buffer, &indices, &program, &glium::uniforms::EmptyUniforms, &Default::default()).unwrap();
                        }
                    }
                }
            }

            target.finish().unwrap();

            // windowed_context.swap_buffers().unwrap();
            // display.swap_buffers().unwrap();
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

    fn get_object(&self, py: Python, name: String) -> PyResult<PyObject> {
        let list: &vec::Vec<PyObject> = &self.object_list.borrow();

        let mut index = 0;
        for obj in list {
            if obj.getattr(py, "name")?.extract::<String>(py)? == name {
                let item = match list.get(index) {
                    Some(item) => (*item).to_object(py),
                    None => py.None()
                };

                return Ok(item)
            }
            index += 1;
        }

        return Ok(py.None())
    }

    fn get_object_with_component(&self, type_: PyObject) {}
}

#[pyclass(gc, subclass)]
struct GameObject {
    scene: cell::RefCell<Option<PyObject>>,
    #[pyo3(get)]
    name: String,
    component_list: cell::RefCell<vec::Vec<PyObject>>,
}

#[pymethods]
impl GameObject {
    #[new]
    fn __new__(obj: &PyRawObject, name: String) -> PyResult<()> {
        Ok(obj.init({ GameObject { scene: cell::RefCell::new(None), name, component_list: cell::RefCell::new(vec::Vec::new()) } }))
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

    // Called when the object is created
    fn start(&self) -> PyResult<()> {
        Ok(())
    }

    // Called once every frame
    fn update(&self) -> PyResult<()> {
        Ok(())
    }

    // Called once every frame, after the update
    fn draw(&self, py: Python) -> PyResult<Option<Py<PyDict>>> {
        Ok(None)
    }

    // Called when the object is destroyed
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
        Component::__new__(obj)?;
        Ok(())
    }
}

#[pyclass(gc, extends = Component)]
struct Camera {
    size: vec::Vec<f32>,
    aspect_ration: f32,
    fov: f32,
    z_plane: vec::Vec<f32>,
}

#[pymethods]
impl Camera {
    #[new]
    fn __new__(obj: &PyRawObject,
               size: vec::Vec<f32>,
               aspect_ration: f32,
               fov: f32,
               z_plane: vec::Vec<f32> ) -> PyResult<()> {
        obj.init({ Camera { size, aspect_ration, fov, z_plane } });
        Component::__new__(obj)?;
        Ok(())
    }
}

#[pyclass(gc, extends = Component)]
struct ShapeRender {}

#[pymethods]
impl ShapeRender {
    #[new]
    fn __new__(obj: &PyRawObject, position: &PyTuple, rotation: &PyTuple, scale: &PyTuple) -> PyResult<()> {
        obj.init({ ShapeRender {} });
        Component::__new__(obj)?;
        Ok(())
    }
}

#[pyclass(gc, extends = ShapeRender)]
struct RectangleRender {
    size: Vector2<f32>,
}

#[pymethods]
impl RectangleRender {
    #[new]
    fn __new__(obj: &PyRawObject, size: &PyTuple) -> PyResult<()> {
        obj.init({
            RectangleRender {
                size: Vector2::new(size.get_item(0).extract()?,
                                   size.get_item(1).extract()?),
            }
        });
        Component::__new__(obj)?;
        Ok(())
    }

    fn update(&self) -> PyResult<()> {
        Ok(())
    }

    fn draw(&self, py: Python) -> PyResult<vec::Vec<PyObject>> {
        let bottom_left = Vertex { position: [-&self.size.x, -&self.size.y] };
        let top_left = Vertex { position: [-&self.size.x, (&self.size).y] };
        let top_right = Vertex { position: [(&self.size).x, (&self.size).y] };
        let bottom_right = Vertex { position: [(&self.size).x, -&self.size.y] };

        let vertices = vec![bottom_left, top_left, bottom_right, bottom_right, top_right, top_left];
        let shader_name = "rectangle";

        let dict = PyDict::new(py);
        dict.set_item("vertices", vertices);
        dict.set_item("shader_name", shader_name);

        Ok(dict.values().extract()?)
    }
}

#[pymodule]
fn swine(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Window>()?;
    m.add_class::<Scene>()?;
    m.add_class::<GameObject>()?;
    m.add_class::<Component>()?;
    m.add_class::<Transform>()?;
    m.add_class::<Camera>()?;
    m.add_class::<ShapeRender>()?;
    m.add_class::<RectangleRender>()?;
    Ok(())
}
