from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(name='swine',
      version="3.0.0",
      rust_extensions=[RustExtension('swine.swine', 'Cargo.toml',  binding=Binding.PyO3)],
      packages=["swine"],
      zip_safe=False)
