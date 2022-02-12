import os
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import (
    Qt,
    QFile,
    QIODevice,
    Slot,
)
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QMainWindow,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtQml import QQmlApplicationEngine

from qt_material import apply_stylesheet

from twisted.internet import reactor
from twisted.internet import task

from guiapp.ui.main import Ui_MainWindow


def main_widgets(app: QApplication):
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec_())


def main_qml(app: QApplication):
    engine = QQmlApplicationEngine()
    qml_file_name = os.fspath(Path(__file__).resolve().parent / "ui/main.qml")
    engine.load(qml_file_name)
    if not engine.rootObjects():
        print(f"Cannot open {qml_file_name}")
        sys.exit(-1)
    sys.exit(app.exec_())


def load_ui(fname):
    ui_file_name = os.fspath(Path(__file__).resolve().parent / fname)
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    return window


# Promote window to main window
class MainWindow(QMainWindow, Ui_MainWindow):
    pass


def main_ui(app: QApplication):

    # setup stylesheet
    apply_stylesheet(app, theme='dark_blue.xml')

    # Load the UI on the fly
    #window = load_ui("ui/main.ui")

    # ..or use the uic class
    window = MainWindow()
    window.setupUi(window)

    @Slot()
    def say_hello():
        print("Button clicked, Hello!")

    window.pushButton.clicked.connect(say_hello)

    # Test that twisted is operational
    task.deferLater(reactor, 3, lambda: print("TWISTED WORKS"))

    window.show()
    app.exec()
    reactor.runReturn()


def main(app: QApplication):

    #main_widgets(app)
    #main_qml(app)
    main_ui(app)
