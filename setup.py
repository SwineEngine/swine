from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(name='swine',
      version="3.0.0",
      rust_extensions=[RustExtension('swine', 'Cargo.toml',  binding=Binding.RustCPython)],
      packages=["swine"],
      zip_safe=False)
