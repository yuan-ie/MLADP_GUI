import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("PyQt6 GUI with Styling")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set a margin around the window
        central_widget.setContentsMargins(20, 20, 20, 20)

        # Main layout
        main_layout = QVBoxLayout()

        # TITLE
        # ----------------------------------------------------------------
        title_label = QLabel("My Application Title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        # Add the title label to the layout with a stretch factor
        main_layout.addWidget(title_label, 0)  # Stretch factor = 0, no extra space is given

        # BUTTONS (Block Two)
        # ----------------------------------------------------------------

        # Create the second block
        block_two = QVBoxLayout()

        # Horizontal Layout for buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)  # Space between buttons
        
        # Create buttons with rounded corners
        button1 = QPushButton("About Me")
        button2 = QPushButton("All Data")
        button3 = QPushButton("Etc.")
        
        # Add buttons to the layout
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        block_two.addLayout(button_layout)

        main_layout.addLayout(block_two)

        # WINDOWS (Block Three)
        # ----------------------------------------------------------------

        block_three = QVBoxLayout()
        window_layout = QHBoxLayout()
        window_layout.setSpacing(30)  # Space between buttons

        # Left window (box)
        left_window = QGroupBox("Left Window")
        left_window.setStyleSheet("background-color: lightblue;")
        left_layout = QVBoxLayout()
        left_window.setLayout(left_layout)
        
        # Right window (box)
        right_window = QGroupBox("Right Window")
        right_window.setStyleSheet("background-color: lightgreen;")
        right_layout = QVBoxLayout()
        right_window.setLayout(right_layout)

        window_layout.addWidget(left_window)
        window_layout.addWidget(right_window)

        # Add content layout to the main layout
        main_layout.addLayout(window_layout)

        # # Other widgets or content (takes up remaining space)
        # content_label = QLabel("Content Below")
        # content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # main_layout.addWidget(content_label, 1)  # Stretch factor = 1, takes up most of the space

        # # Set the layout on the central widget
        # central_widget.setLayout(main_layout)

       
        

        

        main_layout.addStretch(1)

        # Set the central widget layout
        central_widget.setLayout(main_layout)

        # # Apply QSS (Qt Style Sheets) for rounded buttons and padding
        # self.setStyleSheet("""
        #     QPushButton {
        #         border-radius: 15px;
        #         padding: 10px;
        #         background-color: #4CAF50;
        #         color: white;
        #         font-size: 16px;
        #     }

        #     QPushButton:hover {
        #         background-color: #45a049;
        #     }

        #     QPushButton:pressed {
        #         background-color: #3e8e41;
        #     }
        # """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
