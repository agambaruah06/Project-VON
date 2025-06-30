import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

IMAGE_PATH = "../memory/avatar.png"

class AvatarWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Von - Avatar")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #222;")

        # Create layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add image
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(IMAGE_PATH)
        if pixmap.isNull():
            print(f"Error: Could not load image from {IMAGE_PATH}")
        else:
            self.image_label.setPixmap(pixmap.scaled(300, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        layout.addWidget(self.image_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AvatarWindow()
    window.show()
    sys.exit(app.exec_())
