import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class FloatingMic(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 100, 100)

        # Set microphone icon
        self.button = QPushButton('', self)
        mic_icon = QIcon("img.png")  # Ensure this path is correct
        self.button.setIcon(mic_icon)
        self.button.setIconSize(QSize(75, 75))  # Adjust this size as needed
        self.button.setGeometry(0, 0, 100, 100)
        self.button.setStyleSheet("border:5px black; background:transparent;")
        self.button.clicked.connect(self.toggle_program)

        self.is_running = False
        self.process = None
        self.old_pos = self.pos()

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.old_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()

    def toggle_program(self):
        if self.is_running:
            self.stop_program()
        else:
            self.start_program()

    def start_program(self):
        try:
            self.process = subprocess.Popen(["python", "main.py"])  # Start main.py
            self.is_running = True
            print("Program started.")
        except Exception as e:
            print(f"Error starting program: {e}")

    def stop_program(self):
        if self.process:
            self.process.terminate()  # Terminate the running process
            self.process = None
            self.is_running = False
            print("Program stopped.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mic = FloatingMic()
    mic.show()
    sys.exit(app.exec_())
