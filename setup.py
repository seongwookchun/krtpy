from distutils.core import setup
from setuptools import find_packages

setup(name='krt',
  version='alpha1.1.5',
  # py_modules=['engine', 'utils'],
  #package_dir={"": "krt"},
  #packages=find_packages("krt"),
  packages=find_packages(),#['krt'],
  author='Dan Rasband',
  author_email='danrasband@gmail.com',
  url='http://code.google.com/p/krtpy'
)
