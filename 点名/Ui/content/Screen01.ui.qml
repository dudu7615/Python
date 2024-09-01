/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.5
import QtQuick.Controls 6.5
import Ui
import QtQuick.Layouts
import Py

Rectangle {
    id: page
    width: Constants.width
    height: Constants.height
    anchors.fill: parent
    color: Constants.backgroundColor

    Py {
        id: py
    }

    ColumnLayout {
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 10
        anchors.topMargin: 10

        Text {
            id: name
            text: qsTr("此处将显示名字")
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter
            Layout.fillWidth: true
            Layout.preferredWidth: 216
            Layout.preferredHeight: 39
        }

        Button {
            id: run
            text: qsTr("获取随机姓名")
            Layout.leftMargin: 0
            Layout.fillWidth: true

            Connections {
                target: run
                onClicked: name.text = py.run()
            }
        }
    }
}
