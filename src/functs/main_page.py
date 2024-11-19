import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox
from PyQt6.QtCore import Qt

import layouts

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("PyQt6 GUI with Styling")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0d1e1;")

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

        block_two = layouts.menu_block()
        main_layout.addLayout(block_two)

        # WINDOWS (Block Three)
        # ----------------------------------------------------------------

        block_three = layouts.display_block()
        main_layout.addLayout(block_three)
        

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
