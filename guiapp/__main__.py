import os
import sys
from PySide6.QtWidgets import QApplication
import qt5reactor


def main():

    # Force darkmode
    os.environ['QT_QPA_PLATFORM'] = "windows:darkmode=1"

    # Create the main application first due to the twisted singleton usage
    app = QApplication(sys.argv)

    if "twisted.internet.reactor" in sys.modules:
        del sys.modules["twisted.internet.reactor"]

    # Install the pyside2 twisted reactor
    # This must be done before any other twisted imports
    qt5reactor.install()

    # This construct is required ensure twisted reactor is not loaded
    # before the above install
    from guiapp.main import main
    main(app)


# To support -m guiapp
if __name__ == '__main__':
    main()
