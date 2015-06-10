<<<<<<< HEAD
OpenPTV-Python (PyPTV)
======================

**OpenPTV-Python** (a.k.a **PyPTV**) is the Python version of [OpenPTV](http://www.openptv.net). It is basically the Python Traits GUI (from Enthought Inc.) that *interfaces* the OpenPTV library that includes all the core algorithms (correspondence, tracking, calibration, etc.) written in ANSI C. 

Both PyPTV and the OpenPTV library are in the development phase and continuously refactored. Please follow the development on the community mailing list:

	openptv@googlegroups.com


## Documentation, including installation instructions

http://alexlib.github.io/docs/index.html

## Getting started:

If the compilation passed, open the terminal and run:  

		python pyptv_gui/pyptv_gui.py

Follow the instructions in our **screencasts and tutorials**:
  
  *  Tutorial 1: <http://youtu.be/S2fY5WFsFwo>  
  
  *  Tutorial 2: <http://www.youtube.com/watch?v=_JxFxwVDSt0>   
  
  *  Tutorial 3: <http://www.youtube.com/watch?v=z1eqFL5JIJc>  
  
  
Ask for help on our mailing list:

	openptv@googlegroups.com
=======
# OpenPIV

OpenPIV consists in a Python and Cython modules for scripting and executing the analysis of 
a set of PIV image pairs. In addition, a Qt graphical user interface is in 
development, to ease the use for those users who don't have python skills.

## Warning

The OpenPIV python version is currently in alpha state. This means that
it is buggy, untested and the API may change. However testing and contributing
is very welcome, especially if you can contribute with new algorithms and features.

Development is currently done on a Linux/Mac OSX environment, but as soon as possible 
Windows will be tested. If you have access to one of these platforms
please test the code. 

## Installing

We are listed on PyPI: <https://pypi.python.org/pypi/OpenPIV>, so you could just try:

    pip install openpiv

or 

    easy_install openpiv

### To build from source

Download the package from the Github: https://github.com/OpenPIV/openpiv-python/archive/master.zip
or clone using git

    git clone https://github.com/OpenPIV/openpiv-python.git

Using distutils create a local (in the same directory) compilation of the Cython files:

    python setup.py build_ext --inplace

Or for the global installation, use:

    python setup.py install 


### Latest developments

Latest developments go into @alexlib repository <https://github.com/alexlib/openpiv-python>

## Documentation

The OpenPIV documentation is available on the project web page at <http://openpiv.readthedocs.org>


## Contributors

1. Alex Liberzon  
2. Roi Gurka  
3. Zachary J. Taylor  
4. David Lasagna  
5. Mathias Aubert
>>>>>>> dff59293997437104423e00651d71ff4feadc02c

