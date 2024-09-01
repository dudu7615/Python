// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0-only

import QtQuick 6.5
import Ui

Window {
    width: Constants.width
    height: Constants.height
    flags: Qt.Window | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint
//    minimumWidth: Constants.width
//    minimumHeight: Constants.height

    id: win

    visible: true
    title: "计时器"

    Screen01 {
        id: mainScreen
        anchors.fill: parent

    }
}

