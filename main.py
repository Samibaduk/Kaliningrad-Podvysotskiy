import sys
from PIL import Image
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QSlider
from PyQt6.QtGui import QPixmap


class AlphaManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.current = 'orig.jpg'
        self.new_img = 'new.png'
        self.initUI()
        self.alpha.valueChanged.connect(self.change_alpha)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Изменение прозрачности')

        self.pixmap = QPixmap()
        # здравствуйте, Ольга Владимировна
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)

        self.alpha = QSlider(self)
        self.alpha.move(20, 30)
        self.alpha.resize(20, 300)
        self.alpha.setMinimum(0)
        self.alpha.setMaximum(256)
        self.alpha.setValue(255)

    def change_alpha(self):
        transp = int(self.alpha.value())
        img = Image.open(self.current)
        img.putalpha(transp)
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
