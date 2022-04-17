import imp
from setuptools import setup, find_packages
import os

base_version = imp.load_source(
    "aml_setup.version", os.path.join("aml_setup", "version.py")
).VERSION

if os.environ.get("LOCAL_VERSION") is not None:
    version = "%s.%s" % (base_version, os.environ.get("LOCAL_VERSION").replace(".", ""))
else:
    version = base_version

setup(
    name="aml_setup",
    version=version,
    description="AML Setup Example",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "numpy",
        "pandas",
        "pipenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
