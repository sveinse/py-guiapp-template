import QtQuick
import QtQuick.Window

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Text {
        id: text1
        x: 50
        y: 50
        text: qsTr("Hello World")
        font.pixelSize: 12
    }
}
