import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMessageBox
from PyQt6.QtGui import QAction, QKeySequence

class Task3Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Завдання 3")
        
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.textChanged.connect(lambda: self.statusBar().showMessage("Змінено"))

        menubar = self.menuBar()
        toolbar = self.addToolBar("Панель")

        file_menu = menubar.addMenu("Файл")
        help_menu = menubar.addMenu("Довідка")

        clear_act = QAction("Очистити", self)
        clear_act.setShortcut(QKeySequence.StandardKey.Refresh)
        clear_act.triggered.connect(self.editor.clear)

        about_act = QAction("Про програму", self)
        about_act.triggered.connect(lambda: QMessageBox.about(self, "Info", "Лабораторна робота"))

        file_menu.addAction(clear_act)
        help_menu.addAction(about_act)
        toolbar.addAction(clear_act)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task3Window()
    w.show()
    sys.exit(app.exec())
