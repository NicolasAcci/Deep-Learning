#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QMainWindow):  # QWidget  ，QMainWindow

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("3333 ")
        self.label.setFixedSize(220, 250)
        self.label.move(50, 100)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(30, 40)
        btn.clicked.connect(self.openimage)

        btn1 = QPushButton(self)
        btn1.setText("进行监测")
        btn1.move(150, 40)

        btn2 = QPushButton(self)
        btn2.setText("开始识别")
        btn2.move(270, 40)

        btn3 = QPushButton(self)
        btn3.setText("退出")
        btn3.move(390, 40)


        # #按钮提示
        # QToolTip.setFont(QFont('SansSerif', 10))  # 字体
        # self.setToolTip('This is a <b>QWidget</b> widget')
        # btn.setToolTip('这个是用来播放的')  # 按钮提示框的内容
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)


        # 子菜单
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        impAct = QAction('Import mail', self)
        fileMenu_1 = menubar.addMenu('Tool')
        fileMenu_2 = menubar.addMenu('Edit')
        impMenu = QMenu('Import', self)
        impMenu_1 = QMenu('Input', self)
        impMenu.addAction(impAct)
        impMenu_1.addAction(impAct)
        newAct = QAction('New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addMenu(impMenu_1)

        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle('人物监测')
        self.setWindowIcon(QIcon('web.png'))

        self.show()

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def contextMenuEvent(self, event):
        """鼠标右键菜单"""
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    def closeEvent(self, event):
        """退出时，提示是否退出窗口"""

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
