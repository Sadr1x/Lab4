import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QMessageBox, QInputDialog, QDialog, QLineEdit, QFormLayout
)

QSS = """
    QWidget { background-color: #2b2b2b; color: #ffffff; font-size: 14px; }
    QPushButton { background-color: #007acc; border-radius: 4px; padding: 6px; }
    QPushButton:hover { background-color: #005999; }
    QLineEdit { background-color: #3c3f41; border: 1px solid #555; }
"""

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.field = QLineEdit()
        layout.addRow("Введіть значення:", self.field)
        btn = QPushButton("OK")
        btn.clicked.connect(self.accept)
        layout.addWidget(btn)
        self.setLayout(layout)

class Task5Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Завдання 5")
        layout = QVBoxLayout()

        btn1 = QMessageBox.StandardButton
        self.b1 = QPushButton("1. QMessageBox")
        self.b2 = QPushButton("2. QInputDialog")
        self.b3 = QPushButton("3. Власний QDialog")

        self.b1.clicked.connect(lambda: QMessageBox.information(self, "Info", "Стандартний діалог"))
        self.b2.clicked.connect(lambda: QInputDialog.getText(self, "Введення", "Введіть текст:"))
        self.b3.clicked.connect(lambda: CustomDialog().exec())

        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        layout.addWidget(self.b3)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS)  
    w = Task5Window()
    w.show()
    sys.exit(app.exec())
