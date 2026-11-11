import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout, 
    QLabel, QLineEdit, QSpinBox, QComboBox, QCheckBox, QPushButton
)

class Task1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Завдання 1")
        
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введіть текст...")
        self.line_edit.setToolTip("Головне поле введення")

        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 100)
        self.spin_box.setValue(10)

        self.combo = QComboBox()
        self.combo.addItems(["Пункт A", "Пункт B"])

        form_layout.addRow("Текст:", self.line_edit)
        form_layout.addRow("Число:", self.spin_box)
        form_layout.addRow("Вибір:", self.combo)

        self.checkbox = QCheckBox("Погоджуюсь з умовами")
        self.btn = QPushButton("Надіслати")
        self.btn.setEnabled(False)
        self.checkbox.toggled.connect(self.btn.setEnabled)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.checkbox)
        main_layout.addWidget(self.btn)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task1Window()
    w.show()
    sys.exit(app.exec())
