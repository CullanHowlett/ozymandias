import pathlib
from setuptools import setup
from src.ozymandias import __version__

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="ozymandias",
    version=__version__,
    description="Pipeline for extracting cosmology from gravitational waves",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CullanHowlett/ozymandias",
    author="Cullan Howlett",
    author_email="cullan.howlett@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
    ],
    package_dir={"": "src"},
    packages=["ozymandias"],
    python_requires=">=3.10, <4",
    install_requires=[
        "numpy>=1.25.0",
        "scipy>=1.11.0",
        "jax[cpu]",
    ],
    package_data={"ozymandias": ["data/*.txt"]},
    project_urls={
        "Bug Reports": "https://github.com/CullanHowlett/ozymandias/issues",
    },
)
