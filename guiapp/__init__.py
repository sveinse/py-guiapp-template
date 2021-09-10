import sys
from PySide6.QtWidgets import QApplication

# Create the main application first due to the twisted singleton usage
print("CREATE APP")
app = QApplication(sys.argv)

if "twisted.internet.reactor" in sys.modules:
    print("REACTOR PRESENT")
    del sys.modules["twisted.internet.reactor"]

# Install the pyside2 twisted reactor
# This must be done before any other twisted imports
from twisted.application import reactors
print("INSTALL REACTOR")
reactors.installReactor('pyside2')
