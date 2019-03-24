#[macro_use]
extern crate cpython;

use cpython::{Python, PyResult, PyObject};

fn test(py: Python) -> PyResult<(PyObject)> {
    println!("It just works.");
    Ok(py.None())
}

py_module_initializer!(swine, initswine, PyInit_swine, |py, m| {
    m.add(py, "test", py_fn!(py, test()))?;
    Ok(())
});