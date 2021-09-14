# Python GUI App Template

A very small framework for setting up a python project in a virtual environment.
The project adds `pyside6` from Qt to add GUI support.

The project is able to be installed with `pyinstaller` to make self-contained
executables.


## Setup

Install the venv:

    $ py -3 -m venv venv     # Windows
    $ python -m venv venv    # Linux

Update the venv:

    $ venv/Scripts/python.exe -m pip install --upgrade pip wheel   # Windows
    $ venv/bin/pip install --upgrade pip wheel                     # Linux

Install the packages (Use `install -e` to install the current package in-place
for development):

    $ venv/Scripts/pip.exe install -e .[dev,test,install]   # Windows
    $ venv/bin/pip install -e .[dev,test,install]           # Linux

## Make one-dir executable

Windows:
    $ venv\Scripts\pyinstaller.exe --noconfirm --onedir --distpath=dist/ guiapp.spec


## Links

- Qt for Python (pyside6)
  https://wiki.qt.io/Qt_for_Python

- Pyinstaller
  http://www.pyinstaller.org/

- Compiling UI files
  https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html

- Python signals and slots:
  https://wiki.qt.io/Qt_for_Python_Signals_and_Slots

- GUI tutorials
  https://www.pythonguis.com/

- Setup tools
  https://setuptools.readthedocs.io/en/latest/index.html
