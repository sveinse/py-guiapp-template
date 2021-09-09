# Prosject readme

A very small framework for setting up a python project in a virtual environment.
The project adds `pyside6` from Qt to add GUI support.

The project also includes `pyinstaller`

Links:

- https://wiki.qt.io/Qt_for_Python
- http://www.pyinstaller.org/


## Setup

Install the venv:

    $ py -3.7 -m venv venv   # Windows
    $ python -m venv venv    # Linux

Update the venv:

    $ venv\Scripts\python.exe -m pip install --upgrade pip wheel   # Windows
    $ venv/bin/pip install --upgrade pip wheel                     # Linux

Install the packages (Use `install -e` to install the current package in-place
for development):

    $ venv\Scripts\pip.exe install -e .[dev,test,install]   # Windows
    $ venv/bin/pip install -e .[dev,test,install]           # Linux


## Make one-dir executable

   $ venv\Scripts\pyinstaller.exe --noconfirm --onedir --distpath=dist/ guiapp.spec
