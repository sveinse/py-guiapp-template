import sys
from PySide6.QtWidgets import QApplication
import pyside2reactor

# Create the main application first due to the twisted singleton usage
app = QApplication(sys.argv)

if "twisted.internet.reactor" in sys.modules:
    del sys.modules["twisted.internet.reactor"]

# Install the pyside2 twisted reactor
# This must be done before any other twisted imports
pyside2reactor.install()
