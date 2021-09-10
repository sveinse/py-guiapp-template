import os
import sys
from pathlib import Path

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
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from qt_material import apply_stylesheet

from twisted.internet import reactor
from twisted.internet import task

from guiapp import app
from guiapp.ui.main import Ui_MainWindow


def main_widgets():
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec_())


def main_qml():
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


def main_ui():

    ui_file_name = os.fspath(Path(__file__).resolve().parent / "ui/main.ui")
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader(None)
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)

    #window = load_ui("ui/main.ui")

    # setup stylesheet
    apply_stylesheet(app, theme='dark_blue.xml')

    @Slot()
    def say_hello():
        print("Button clicked, Hello!")

    button = window.findChild(QWidget, "pushButton")
    button.clicked.connect(say_hello)

    task.deferLater(reactor, 5, lambda: print("HEPPS"))

    window.show()
    app.exec()
    reactor.runReturn()


def main_uic():

    class Ui_MainWindow_User(Ui_MainWindow):
        @Slot()
        def say_hello(self):
            print("Button clicked, Hello!")
        def setupUi(self, MainWindow):
            super().setupUi(MainWindow)
            self.pushButton.clicked.connect(self.say_hello)

    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow_User()
            self.ui.setupUi(self)

    window = MainWindow()

    # setup stylesheet
    apply_stylesheet(app, theme='dark_blue.xml')

    task.deferLater(reactor, 5, lambda: print("HEPPS"))

    window.show()
    app.exec_()
    reactor.runReturn()


def main():
    print("MAIN")

    if "twisted.internet.reactor" in sys.modules:
        print("REACTOR PRESENT (MAIN)")
    #    del sys.modules["twisted.internet.reactor"]

    #main_widgets()
    #main_qml()
    main_ui()
    #main_uic()
