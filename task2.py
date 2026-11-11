import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, 
    QSlider, QCheckBox, QPushButton, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt

class Task2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Завдання 2")
        
        layout = QVBoxLayout()
        self.input_text = QLineEdit()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider_label = QLabel("50")
        self.checkbox = QCheckBox("Активувати кнопку")
        self.submit_btn = QPushButton("OK")
        self.submit_btn.setEnabled(False)
        self.reset_btn = QPushButton("Скинути")

        layout.addWidget(QLabel("Текст:"))
        layout.addWidget(self.input_text)
        layout.addWidget(self.slider)
        layout.addWidget(self.slider_label)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.submit_btn)
        layout.addWidget(self.reset_btn)
        self.setLayout(layout)

     
        self.checkbox.toggled.connect(self.submit_btn.setEnabled)
        
     
        self.slider.valueChanged.connect(lambda v: self.slider_label.setText(str(v)))
     
        self.input_text.textChanged.connect(lambda t: print(f"Введено: {t}"))
    
        self.submit_btn.clicked.connect(self.validate)
        self.reset_btn.clicked.connect(self.reset_form)

    def validate(self):
        if len(self.input_text.text()) < 3:
            QMessageBox.warning(self, "Помилка", "Текст занадто короткий!")
        else:
            QMessageBox.information(self, "Успіх", "Дані коректні!")

    def reset_form(self):
        self.input_text.clear()
        self.slider.setValue(50)
        self.checkbox.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task2Window()
    w.show()
    sys.exit(app.exec())
