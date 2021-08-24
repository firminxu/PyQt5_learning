import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color = yellow> This is a Label")
        label1.setAutoFillBackground(True)
        patette = QPalette()
        patette.setColor(QPalette.Window, Qt.blue)#设置背景色
        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href = '#'>Welcome to use python GUI")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('This is a picture')
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://www.jd.com> thank to focus</a>'")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('This is a link')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel demo")

    def linkHovered(self):
        print('When mouse slide label2, active')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
