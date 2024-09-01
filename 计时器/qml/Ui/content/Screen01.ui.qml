

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import QtQuick.Layouts
import QtQuick3D
import Ui
import py

Rectangle {
    width: Constants.width
    height: Constants.height
    id: root
    color: Constants.backgroundColor

    Py {
        id: py
    }
    //    App{
    //        id:root
    //    }
    Connections {
        target: start
        onCheckedChanged: {
            if (chooseTime.value != 0) {
                py.start(start.checked)

                if (start.checked) {
                    start.text = qsTr("计时中")
                } else {
                    start.text = qsTr("计时停止")
                }
            } else {
                start.checked = false
            }
        }
    }

    Connections {
        target: chooseTime
        onValueChanged: {
            py.changeTime(chooseTime.value)
            start.checked = false
        }
    }

    Connections {
        target: py
        function onSignal(time) {
            showTime.text = time
        }
    }

    Connections {
        target: root

        onWidthChanged: {
            showTime.font.pixelSize = root.width / 3
            win.minimumHeight = showTime.font.pixelSize
        }

        onHeightChanged: {
            showTime.font.pixelSize = root.width / 3
            win.minimumHeight = showTime.font.pixelSize
        }
    }

    GridLayout {
        anchors.fill: parent
        rows: 2
        columns: 2

        Text {
            id: showTime
            opacity: 1
            text: qsTr("00:00")
            elide: Text.ElideMiddle
            font.pixelSize: 110
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WrapAnywhere
            Layout.preferredHeight: 140
            Layout.preferredWidth: 350
            textFormat: Text.PlainText
            Layout.fillWidth: true
            scale: 1
            font.styleName: "Regular"
            rotation: 0
            Layout.columnSpan: 2
            font.bold: true
        }

        Slider {
            id: chooseTime
            pressed: false
            live: true
            clip: false
            wheelEnabled: false
            spacing: 0
            topPadding: 0
            leftPadding: 10
            Layout.fillWidth: true
            stepSize: 1
            to: 45
            Layout.preferredHeight: 22
            Layout.preferredWidth: 241
            value: 0
        }

        Switch {
            id: start
            text: qsTr("计时停止")
            checked: false
            Layout.fillWidth: true
            Layout.preferredHeight: 28
            Layout.preferredWidth: 123
        }
    }

    Item {
        id: __materialLibrary__
    }

    DirectionalLight {
        id: lightDirectional
        x: 20.924
        y: -84.665
        brightness: 5.24
        z: 154.03929
    }
}
