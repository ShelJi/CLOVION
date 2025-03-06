################# boilerplate #######################

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
        
# if __name__ == "__main__":
#     main()


import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QBoxLayout, QHBoxLayout, QGridLayout,
                             QPushButton  )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("CooooL")
        x, y, width, height = 420, 150, 500, 500
        self.setGeometry(x, y, width, height)
        self.setWindowIcon(QIcon("eeee.jpg"))
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 100, 100)
        label.setStyleSheet("color: pink;"
                            "background: Blue;")
        label.setAlignment(Qt.AlignCenter)
        
        
        label1 = QLabel(self)
        label1.setGeometry(100, 100, 300, 300)
        label1.setPixmap(QPixmap("eeee.jpg"))
        label1.setScaledContents(True)
        label1.setGeometry((self.width() - label1.width()) // 2,
                           (self.height() - label1.height()) // 2,
                           label1.width(),
                           label1.height())
        
        def initUI(self):
            ...
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    main()