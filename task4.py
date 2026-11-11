import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal

class Sender(QWidget):
    data_sent = pyqtSignal(str)  

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.input = QLineEdit()
        btn = QPushButton("Надіслати")
        btn.clicked.connect(lambda: self.data_sent.emit(self.input.text()))
        layout.addWidget(self.input)
        layout.addWidget(btn)
        self.setLayout(layout)

class Receiver(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Очікування даних...")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def receive_data(self, text):
        self.label.setText(f"Отримано: {text}")

class Task4Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Завдання 4")
        layout = QVBoxLayout()

        self.sender = Sender()
        self.receiver = Receiver()

      
        self.sender.data_sent.connect(self.receiver.receive_data)

        
        self.disc_btn = QPushButton("Вимкнути зв'язок")
        self.disc_btn.clicked.connect(lambda: self.sender.data_sent.disconnect(self.receiver.receive_data))

        layout.addWidget(self.sender)
        layout.addWidget(self.receiver)
        layout.addWidget(self.disc_btn)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task4Main()
    w.show()
    sys.exit(app.exec())
