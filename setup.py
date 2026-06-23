"""
Python packaging configuration for dab_project. This file defines how to build and
distribute the project as a Python wheel package. When deploying a wheel with DAB,
the command `python setup.py bdist_wheel` is executed by default to create a
distributable .whl file that can be installed in other Python environments.
"""

from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains the code in the src directory for the DAB project",
    author="TM",
    packages=find_packages(
        where="./src"
    ),  # This tells setuptools to look for packages in the 'src' directory
    package_dir={
        "": "src"
    },  # This tells setuptools that the root package is in the 'src' directory
    install_requires=[
        # List your project dependencies here, e.g.:
        "setuptools",
    ],
    # entry_points={
    #     "packages": [
    #         "main=dab_project.main:main",
    #     ],
    # },
)

# run this script with the command `python setup.py bdist_wheel` to create a wheel distribution of your project.
# This will generate a .whl file in the dist directory, which you can then install using:
#   > pip install dist/dab_project-0.0.1-py3-none-any.whl.

# We can install this wheel in our virtual environment using the command `pip install dist/dab_project-0.0.1-py3-none-any.whl`.

# After installing the wheel, we can import the modules from the src directory like this:
# > from citibike import *
#
# We don't need to add the src directory to the sys.path anymore because
# setup script set src as the root package directory.
